from django.shortcuts import render,redirect
from .models import news_db
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def Home_page(request):
    
    news_data = news_db.objects.all()
    data = {"news_data": news_data}


    return render(request,"index.html",data)

def Login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('upload')
    data = {}

    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")

        if Username == "" and Password == "":
            return render(request, "login.html", {'error1': True, 'error2': True})
        elif Username == "" and Password != "":
            data = {'Password': Password}
            return render(request, "login.html", {'error1': True, **data})
        elif Username != "" and Password == "":
            data = {'Username': Username}
            return render(request, "login.html", {'error2': True, **data})
        else:
            
            return login_view(request)
    return render(request, "login.html",**data)

def login_view(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        
        
        user=authenticate(request, username = Username, password = Password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('upload') + '?username=' + Username)
            
        else:
            return render(request, "login.html", {'error3':True})

@login_required(login_url='login')
def upload_view(request):
    if request.method == "POST":
        Title = request.POST.get("title")
        Content = request.POST.get("content")
        if Title == "" and Content == "":
            return render(request, "upload.html", {'error1': True, 'error2': True})
        elif Title == "" and Content != "":
            data = {'Content': Content}
            return render(request, "upload.html", {'error1': True, **data})
        elif Title != "" and Content == "":
            data = {'Title': Title}
            return render(request, "upload.html", {'error2': True, **data})
        else:
            return upload_req(request)
    return render(request, "upload.html")


def logout_view(request):
    logout(request)
    return redirect('/')

def upload_req(request):
    if request.method == "POST":
        Title = request.POST.get('title')
        Content = request.POST.get("content")
        Author = request.POST.get("author")

        if not Title or not Content:
            return upload_view(request)

        en = news_db.objects.create(title=Title, content=Content, author=Author)
        en.save()

        return redirect('home')

    return redirect('upload') 