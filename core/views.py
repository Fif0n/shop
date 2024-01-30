from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileDataForm, ProfilePasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import User
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

@login_required
def profile(request):
    if request.method == 'POST':
        updateType = request.POST.get('update')

        user = request.user

        if updateType == 'profile':
            username = request.POST.get('username')
            email = request.POST.get('email')

            user.username = username
            user.email = email

            if User.objects.filter(username=username).exclude(pk=user.pk).exists():
                messages.info(request, 'Użytkownik o takiej nazwie już istnieje')

                return redirect('/profile/')
            
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                messages.info(request, 'Użytkownik o takiej nazwie już istnieje')

                return redirect('/profile/')

            user.save()

            messages.info(request, 'Zaktualizowano dane')

            return redirect('/profile/')
        
        if updateType == 'password':
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password1')

            if password1 != password2:
                messages.info(request, 'Hasła nie są takie same')
            
            user.set_password(password1)

            user.save()

            update_session_auth_hash(request, user)
            messages.info(request, 'Zaktualizowano hasło')

            return redirect('/profile/')

            
    else:
        formProfile = ProfileDataForm({
            'username': request.user.username,
            'email': request.user.email
        })

        formPassword = ProfilePasswordForm()

    return render(request, 'core/profile.html', {
        'formProfile': formProfile,
        'formPassword': formPassword
    })
