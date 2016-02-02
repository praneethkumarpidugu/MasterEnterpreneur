from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterForm, LoginForm
from accounts.models import MyUser
from comments.models import Comment
from videos.models import Video
from analytics.signals import page_view


#@login_required(login_url='/enroll/login/')
# @login_required
def home(request):
    page_view.send(
        request.user,
        page_path=request.get_full_path(),
    )
    if request.user.is_authenticated():
        page_view_objs = request.user.pageview_set.get_videos()[:6]#number of recent videos
        recent_videos = []
        for obj in page_view_objs:
            if not obj.primary_object in recent_videos:
                recent_videos.append(obj.primary_object)
        recent_comments = Comment.objects.recent()
        context = {
                    "recent_videos": recent_videos,
                    "recent_comments": recent_comments,
                   }
        template = "home_logged_in.html"
    else:
        login_form = LoginForm()
        register_form = RegisterForm()
        template = "home_visitor.html"
        context = {"register_form": register_form, "login_form": login_form}
    return render(request, template , context)
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


