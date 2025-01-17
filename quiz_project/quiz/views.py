from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "quiz/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
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
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


@login_required
def dashboard_view(request):
    quiz_history = QuizResult.objects.filter(user=request.user).order_by("-date_taken")
    return render(request, "quiz/dashboard.html", {"quiz_history": quiz_history})


def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    # print(questions)

    if request.method == "POST":
        correct_answers = 0
        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")
            correct_option = question.options.filter(is_correct=True).first()
            if correct_option and selected_option_id:
                if selected_option_id == str(correct_option.id):
                    correct_answers += 1

        QuizResult.objects.create(user=request.user, quiz=quiz, score=correct_answers)
        return HttpResponseRedirect(f"/quiz/results/{quiz.id}/?correct_answers={correct_answers}")

    return render(request, "quiz/take_quiz.html", {"quiz": quiz, "questions": questions})


def results_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    correct_answers = int(request.GET.get("correct_answers", 0))
    return render(request, "quiz/results.html", {"quiz": quiz, "correct_answers": correct_answers})



def quiz_list(request):
    quizzes = Quiz.objects.all()  # Fetch all quizzes from the database
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})
