from django.shortcuts import render
from .models import *
import score_method

# Create your views here.
def index(request):
    x = EventParticipants.objects.all()
    data = {
        'total_participants' : len(x) if len(x) else '',
        'participants' : x,
        'error' : '',
    }
    if request.method == "POST":
        handle = request.POST.handle
        if EventParticipants.objects.filter(handle=handle):
            data['error'] = "이미 존재하는 handle입니다."
            return render(request,'baekjoon/event.html', data)
        event_object = EventParticipants.objects.create(
            handle=handle,
            score = 0
        )
        event_object.save()
    return render(request,'baekjoon/event.html', data)
