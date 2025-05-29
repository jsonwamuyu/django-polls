import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

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


"""
Pizza Toppings class with M:N relationship

By default Django will automatically create for you a join table
buy you can choose to explicitly add you own with some extra fields 
by creating a 'through' table.
If you need extra data on the relationship, use a through model.

Put the field on the model that logically owns or uses the other.
"""

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)
    toppings = models.ManyToManyField('Toppings',through="PizzaToppings")

class Toppings(models.Model):
    topping_name = models.CharField(max_length=50)

# A through table
class PizzaToppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Toppings, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50) # e.g 'none', 'light', 'extra'


"""
For example, consider the case of an application tracking the musical groups which musicians belong to. 
There is a many-to-many relationship between a person and the groups of which they are a member,
 so you could use a ManyToManyField to represent this relationship. However, there is a lot of
  detail about the membership that
 you might want to collect, such as the date at which the person joined the group.
"""

class MusicGroup(models.Model):
    group_name = models.CharField(max_length=100)
    singers = models.ManyToManyField('Singer', through="MusicGroupMembership")

    def __str__(self):
        return self.group_name

class Singer(models.Model):
    singer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.singer_name


# A through table to join MusicGroup and Singer models
class MusicGroupMembership(models.Model):
    music = models.ForeignKey(MusicGroup, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['singer', 'music'], name='unique_person_group'
            )
        ]