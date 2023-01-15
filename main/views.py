from django.shortcuts import render
import requests
import os
from main.forms import *
from django.contrib.auth import authenticate, login, logout

def home(request):    
    return render(request,"main/home.html")

def user_login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            
        else:
            # Return an 'invalid login' error message.
            return render(request,"")
        
    else:
        return render()
            

def write_blog_post(request):
    
    if request.method == "POST":
        
        form = SubjectForm(request.POST)
        
        if form.is_valid():
        
            headers = {
            'Authorization': 'Bearer '+ os.environ["openai_api_key"],
            }

            json_data = {
                'model': 'text-davinci-003',
                'prompt': 'Write a blog post about ' + form.cleaned_data["subject"],
            }

            response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
            print(response.json())
            
            return render(request,"main/last.html",{"answer":response.json()["choices"][0]["text"]})
        
    else:
        
        form = SubjectForm()
        return render(request,"main/text_input.html",{"form":form})

def text_to_code(request):
    
    if request.method == "POST":
        
        form = TextForm(request.POST)
        
        if form.is_valid():
        
            headers = {
            'Authorization': 'Bearer '+ os.environ["openai_api_key"],
            }

            json_data = {
                'model': 'code-cushman-001',
                'prompt': 'Can you write a code? Subject is ' + form.cleaned_data["text"],
            }

            response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
            print(response.json())
            
            return render(request,"main/last.html",{"answer":response.json()["choices"][0]["text"]})
        
    else:
        
        form = TextForm()
        return render(request,"main/text_input.html",{"form":form})
    
def explain_code(request):
    
    if request.method == "POST":
        
        form = CodeForm(request.POST)
        
        if form.is_valid():
        
            headers = {'Authorization': 'Bearer '+ os.environ["openai_api_key"]}

            json_data = {
                'model': 'code-davinci-002',
                'prompt': 'What does this code do?' + form.cleaned_data["code"],
            }

            response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
            print(response.json())
            
            return render(request,"main/last.html",{"answer":response.json()["choices"][0]["text"]})
        
    else:
        
        form = CodeForm()
        return render(request,"main/code_input.html",{"form":form})