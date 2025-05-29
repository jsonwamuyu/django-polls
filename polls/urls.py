from django.urls import path

from . import views
from .api_views import QuestionListCreateAPIView, QuestionDetailAPIView, ChoiceListCreateAPIView, ChoiceDetailAPIView


app_name = 'polls' # This is required for namespacing

urlpatterns = [
    # ex: /polls/
    path("", views.index, name='index'),
    # ex: /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name='results'),
    # ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name='vote'),

    # /polls/contact-me/
    path("contact-me/", views.contact_me_view, name='contact-me'),

    # Register DRFs API endpoints
    path("api/questions/", QuestionListCreateAPIView.as_view(), name="question-list"),
    path("api/questions/<int:pk>/", QuestionDetailAPIView.as_view(), name="question-detail"),

    path("api/choices/", ChoiceListCreateAPIView.as_view(), name="choice-list"),
    path("api/choices/<int:pk>/", ChoiceDetailAPIView.as_view(), name="choice-detail")
]