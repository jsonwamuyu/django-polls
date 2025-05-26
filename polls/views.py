from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question
from django.template import loader

def index(request):
    """Display latest 5 polls questions by publication date"""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context  = {"latest_question_list":latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id )

def results(request, question_id):
    response = "You are looking at results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You are voting on question %s"
    return HttpResponse(response % question_id)

