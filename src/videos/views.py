from django.core.urlresolvers import reverse
from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from comments.forms import CommentForm
from comments.models import Comment

from .models import Video,Category, TaggedItem


#@login_required
def video_detail(request, cat_slug, vid_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    obj = get_object_or_404(Video, slug=vid_slug, category=cat)
    if request.user.is_authenticated() or obj.has_preview:
        comments = obj.comment_set.all()
        for c in comments:
            c.get_children()
        comment_form = CommentForm()
        context = {"obj": obj,
                   "comments": comments,
                   "comment_form": comment_form }
        return render(request, "videos/video_detail.html", context)
    else:
        next_url = obj.get_absolute_url()
        return HttpResponseRedirect("%s?next=%s" % (reverse('login'), next_url))

def category_list(request):
    queryset = Category.objects.all()
    context = {
        "queryset" : queryset,
    }
    return render(request,"videos/category_list.html", context)

# @login_required
def category_detail(request, cat_slug):
    obj = get_object_or_404(Category, slug=cat_slug)
    queryset = obj.video_set.all()
    print queryset
    return render(request, "videos/video_list.html", {"obj": obj, "queryset": queryset})
