from django.contrib import admin
from django.urls import path, include

# Register apps urls here
urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include('polls.urls', namespace='polls')),
    # path('', views.home)
]
