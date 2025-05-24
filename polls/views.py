from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    """Display latest 5 polls questions by publication date"""
    latest_question_list = Question.objects.order_by("pub_date")
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id )

def results(request, question_id):
    response = "You are looking at results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You are voting on question %s"
    return HttpResponse(response % question_id)

