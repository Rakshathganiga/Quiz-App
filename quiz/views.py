from django.http import JsonResponse
from django.shortcuts import render
from .models import Question, UserPerformance
from django.db.models import Func
from django.db import transaction

class RandomRow(Func):
    function = 'RAND'

def dashboard(request):
    performance = UserPerformance.objects.first()
    if not performance:
        performance = UserPerformance.objects.create()
    context = {
        'total_attempts': performance.total_attempts,
        'correct_answers': performance.correct_answers,
        'score_percentage': (performance.correct_answers / performance.total_attempts * 100) if performance.total_attempts > 0 else 0
    }
    return render(request, 'dashboard.html', context)

def quiz_page(request):
    question = Question.objects.order_by(RandomRow()).first()
    return render(request, 'quiz_page.html', {'question': question})

def submit_answer(request):
    if request.method == "POST":
        question_id = request.POST['question_id']
        selected_option = request.POST['selected_option']
        question = Question.objects.get(id=question_id)

        with transaction.atomic():
            performance = UserPerformance.objects.first()
            if not performance:
                performance = UserPerformance.objects.create()

            performance.total_attempts += 1
            is_correct = selected_option == question.correct_option
            if is_correct:
                performance.correct_answers += 1
            performance.save()

        return JsonResponse({
            'correct': is_correct,
            'feedback': f"{'Correct!' if is_correct else f'Incorrect. The correct answer is {question.correct_option}.'}"
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
