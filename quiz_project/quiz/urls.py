from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    path("dashboard/", dashboard_view, name="dashboard"),
    path('take_quiz/<int:quiz_id>/', take_quiz, name='take_quiz'),
    path('quiz/results/<int:quiz_id>/', results_view, name='results'),
    path('quizzes/', Quizzes, name='quiz_list'),

    path('<path:extra>', handle_extra_path, name='handle_extra'),
]
