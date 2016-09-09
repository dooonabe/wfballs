from django.shortcuts import render, render_to_response


# Create your views here.
def addcoach(request):
    return render_to_response('addCoach.html')


def write_to_base(request):
    return render_to_response('formSuccess.html')


def index(request):
    return render_to_response('index.html')
