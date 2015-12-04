from django.shortcuts import render, HttpResponseRedirect
from django.utils.safestring import mark_safe
from videos.models import Video
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


#@login_required(login_url='/enroll/login/')
@login_required
def home(request):
        name = "Praneeth"
        videos = Video.objects.all()
        embeds = []
        for vid in videos:
            code = mark_safe(vid.embed_code)
            embeds.append("%s" % (code))
        context = {
            "the_name" : name,
            "number" : videos.count(),
            "videos" : videos,
            "the_embeds" : embeds,
            "a_code" : mark_safe(videos[0].embed_code),
        }
        return render(request, "home.html", context)
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


def login(request):
    form = LoginForm()
    context = {
        "form" : form,
    }
    return render(request, "login.html", context)