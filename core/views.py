from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

from item.models import Item

def index(request):
    items = Item.objects.order_by('created_at').all()[:6]

    return render(request, 'core/index.html', {
        'items': items
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Poprawnie zarejestrowano użytkownika')

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_user(request):
    name = request.user.username
    logout(request)
    messages.info(request, 'Wylogowano użytkownika ' + name)

    return redirect('/')
