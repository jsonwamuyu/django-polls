from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world, You are at the index of poll page.")

def login(request):
    return HttpResponse("Login page")

def signup(request):
    return HttpResponse('Create your account.g')