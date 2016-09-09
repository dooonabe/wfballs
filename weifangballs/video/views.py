from django.shortcuts import render_to_response

# Create your views here.


def video_index(request):
    return render_to_response('video_index.html')