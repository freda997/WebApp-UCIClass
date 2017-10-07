from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from online.models import User

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

# Register
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # Acquire form data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # Add to database
            User.objects.create(username = username, password=password)
            return HttpResponse('Register success.')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf})

# Login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # Acquire form data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # Compare with database
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # User info matched, jump to index
                response =  HttpResponseRedirect('/online/index/')
                # Include username in Cookie, expire after 3600s
                response.set_cookie('username', username, 3600)
                return response
            else:
                # Match failure, return to login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf':uf})

# Index
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username':username})

# Logout
def logout(req):
    response = HttpResponse('Logout.')
    # clean username from Cookie
    response.delete_cookie('username')
    return response