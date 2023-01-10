from django.shortcuts import render
import requests

def home(request):


    return render(request,"main/home.html",{"data":"a"})

def get_text(request):
    return render(request,"main/text_input.html")