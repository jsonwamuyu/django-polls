import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Musician(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M":"Medium",
        "L":"Large"
    }
    fullname= models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)

    # Given a model instance, the display value for a field with choices can
    # be accessed using the get_FOO_display() method. For example:
    # e.g p = Musician('Jeff', 'Violin', 'L)
    # p.save()
    # p.shirt_size // 'L'
    # p.get_shirt_size_display() // will display the value -> 'Large'

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    ratings = models.IntegerField()