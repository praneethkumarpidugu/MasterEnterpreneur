from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.
from .forms import LoginForm, RegisterForm
from .models import MyUser

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print username, password
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url is not None:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect("/")

    action_url = reverse("login")
    title = "Login"
    submit_btn = title
    submit_btn_class = "btn-success btn-block"
    extra_form_link = "Upgrade your account today! <a href='%s'>here</a>" %(reverse("account_upgrade"))
    context = {
        "form" : form,
        "action_url": action_url,
        "title": title,
        "submit_btn": submit_btn,
        "submit_btn_class": submit_btn_class,
        "extra_form_link": extra_form_link
    }
    return render(request, "accounts/account_login_register.html", context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def auth_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        # MyUser.objects.create_user(username=username, email=email, password=password)
        new_user = MyUser()
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
    context = {
            "form" : form,
            "action_value" : "",
            "submit_btn_value": "Register",
        }

    action_url = reverse("register")
    title = "Login"
    submit_btn = "Create Free Account"
    context = {
        "form" : form,
        "action_url": action_url,
        "title": title,
        "submit_btn": submit_btn,
    }
    return render(request, "accounts/account_login_register.html", context)
