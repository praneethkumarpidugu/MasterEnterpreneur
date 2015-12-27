from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from comments.forms import CommentForm
from comments.models import Comment

from .models import Video,Category


@login_required
def video_detail(request, cat_slug, vid_slug):
    try:
        cat = Category.objects.get(slug=cat_slug)
    except:
        raise Http404

    try:
        obj = Video.objects.get(slug=vid_slug)
        comments = obj.comment_set.all()
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data['comment']
            new_comment = Comment.objects.create_comment(
                user=request.user,
                path=request.get_full_path(),
                text=comment_text,
                video=obj)
            #add comment thread and show that thread with a message
            return HttpResponseRedirect(obj.get_absolute_url())

        return render(request, "videos/video_detail.html", {"obj": obj, "comments": comments, "comment_form": comment_form })
    except:
        raise Http404

def category_list(request):
    queryset = Category.objects.all()
    context = {
        "queryset" : queryset,
    }
    return render(request,"videos/category_list.html", context)

@login_required
def category_detail(request, cat_slug):

    try:
        obj = Category.objects.get(slug=cat_slug)
        queryset = obj.video_set.all()
        return render(request, "videos/video_list.html", {"obj": obj, "queryset": queryset})
    except:
        raise Http404