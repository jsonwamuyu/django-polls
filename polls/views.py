from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice
from django.template import loader
from django.urls import reverse

from django.http import Http404

def index(request):
    """Display latest 5 polls questions by publication date"""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context  = {"latest_question_list":latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return render(request, "polls/detail.html", {"question":question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})


def results(request, question_id):
    """Display the vote result for the question"""
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html",
                      {"question":question, "error_message":"You did not select a choice"})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice
        # if a user hits the BACK button.
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


