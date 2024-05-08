from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "homepage.html")

def test(request):
    return render(request, "test.html")

def redirect_homepage(request):
    return redirect("/homepage")