from django.http import HttpResponse

from .models import Choice, Question

# from django.shortcuts import render

# Create your views here.


def index(request):
    latest_question_list = Question.objects.filter('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at responses of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
