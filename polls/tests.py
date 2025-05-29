from django.test import TestCase
from polls.models import Question


# Test the Question model
class QuestionModelTest(TestCase):
    def test_string_representation(self):
        question = Question("Going hunting?")
        self.assertEqual(str(question), "Going hunting?")
