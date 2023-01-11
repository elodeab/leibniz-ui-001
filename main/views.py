from django.shortcuts import render
import requests
import os

def home(request):
    
    return render(request,"main/home.html")

def get_text(request):
    return render(request,"main/text_input.html")