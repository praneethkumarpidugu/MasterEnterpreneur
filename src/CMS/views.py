from django.shortcuts import render

__author__ = 'praneethkumar'

def home(request):
    name = "Praneeth"
    context = {
        "the_name" : name,
    }
    return render(request, "base.html", context)