from django.shortcuts import render
from django.utils.safestring import mark_safe
from videos.models import Video

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
    }
    return render(request, "home.html", context)
    #return render_to_response("home.html", context, context_instance=RequestContext(request))