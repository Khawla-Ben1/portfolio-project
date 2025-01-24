from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *


def register_view(request):
    if request.user.is_authenticated:
        # Redirect to dashboard if user is already logged in
        return redirect('dashboard')
    if request.method == "POST":
        # Create a new user
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "quiz/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        # Redirect to dashboard if user is already logged in
        return redirect('dashboard')
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # Authenticate the user
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "quiz/login.html", {"form": form})


def logout_view(request):
    #  Log out the user
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


@login_required
def dashboard_view(request):
    # Fetch all quiz results for the logged-in user
    quiz_history = QuizResult.objects.filter(user=request.user).order_by("-date_taken")
    return render(request, "quiz/dashboard.html", {"quiz_history": quiz_history})


def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == "POST":
        correct_answers = 0
        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")
            correct_option = question.options.filter(is_correct=True).first()
            if correct_option and selected_option_id:
                if selected_option_id == str(correct_option.id):
                    correct_answers += 1
        # Save the result
        QuizResult.objects.create(user=request.user, quiz=quiz, score=correct_answers)
        return HttpResponseRedirect(f"/quiz/results/{quiz.id}/?correct_answers={correct_answers}")

    return render(request, "quiz/take_quiz.html", {"quiz": quiz, "questions": questions})


def results_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    correct_answers = int(request.GET.get("correct_answers", 0))
    total_questions = quiz.questions.count()
    incorrect_answers = total_questions - correct_answers
    #check the score
    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    passed = score_percentage >= 50
    chart_data = {
        'correct': correct_answers,
        'incorrect': incorrect_answers,
        'total': total_questions
    }
    #check the data so the chart will be displayed correctly
    return render(request, "quiz/results.html", {
        "quiz": quiz,
        "correct_answers": correct_answers,
        "total_questions": total_questions,
        "chart_data": chart_data,
        "score_percentage": score_percentage,
        "passed": passed
    })


def Quizzes(request):
    # Fetch all quizzes from the database
    quizzes = Quiz.objects.all() 
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})


def home_view(request):
    if request.user.is_authenticated:
        # Render dashboard for authenticated users
        return render(request, "quiz/dashboard.html") 
    else:
        return redirect('quiz/login')


def handle_extra_path(request, extra):
    #handle 404
    return render(request, 'quiz/404.html', status=404)


