from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterForm
from accounts.models import MyUser
from videos.models import Video

from .forms import LoginForm


#@login_required(login_url='/enroll/login/')
# @login_required
def home(request):
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

            #ADD MESSAGE FOR SUCCESS
            return redirect('login')
            #email user
            # create user profile instance

        # name = "Praneeth"
        # videos = Video.objects.all()
        # embeds = []
        # for vid in videos:
        #     code = mark_safe(vid.embed_code)
        #     embeds.append("%s" % (code))
        context = {
            "form" : form,
            "action_value" : "",
            "submit_btn_value": "Register",
            # "the_name" : name,
            # "number" : videos.count(),
            # "videos" : videos,
            # "the_embeds" : embeds,
            # "a_code" : mark_safe(videos[0].embed_code),
        }
        return render(request, "form.html", context)
        #return render_to_response("home.html", context, context_instance=RequestContext(request))


#
# def home(request):
#         if request.user.is_authenticated():
#             name = "Praneeth"
#             videos = Video.objects.all()
#             embeds = []
#             for vid in videos:
#                 code = mark_safe(vid.embed_code)
#                 embeds.append("%s" % (code))
#             context = {
#                 "the_name" : name,
#                 "number" : videos.count(),
#                 "videos" : videos,
#                 "the_embeds" : embeds,
#                 "a_code" : mark_safe(videos[0].embed_code),
#             }
#             return render(request, "home.html", context)
#             #return render_to_response("home.html", context, context_instance=RequestContext(request))
#
#         #required to login
#         else:
#             return HttpResponseRedirect('/login/')
#

@login_required(login_url='/staff/login')
def staff_home(request):
        context = {

        }
        return render(request, "home.html", context)
        #return render_to_response("home.html", context, context_instance=RequestContext(request))


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
            return HttpResponseRedirect(next_url)
    context = {
        "form" : form,
    }
    return render(request, "login.html", context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
