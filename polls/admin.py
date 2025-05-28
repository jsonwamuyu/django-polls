from django.contrib import admin
from .models import Question, Choice

# Reorder the field for admin page

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"]})
    ]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)