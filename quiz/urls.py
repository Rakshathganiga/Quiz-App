from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz_page, name='quiz_page'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
]
