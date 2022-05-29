from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      return redirect('home')
    return redirect('account:signup')
    
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form' : form})