from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import models, transaction
from django.urls import path
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)

class UserPerformance(models.Model):
    total_attempts = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)

