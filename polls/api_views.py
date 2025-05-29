# import DRFs
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice


    # DRFs and Serializers
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    # Will list(Get) and Create(Post)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Will Get Retrieve(Get) Update(Put) and Destroy(Delete) and object using id
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
