from django.shortcuts import render
from .models import *
from . import score_method
from . import import_info_from_api as api
import time

def makeTimeCheck(cur_time):
    TimeCheck.objects.create(
        last_day=cur_time
    ).save()

# Create your views here.
def index(request):
    x = EventParticipants.objects.all().order_by('score')[::-1]
    data = {
        'total_participants' : len(x) if len(x) else '',
        'user_list' : x,
        'error' : '',
    }

    cur_time = time.ctime().split()
    cur_time = (cur_time[1]+cur_time[2]).strip()
    try:  
        time_obj = TimeCheck.objects.get(pk=1)
        if time_obj.last_day != cur_time:
            print(cur_time,time_obj)
            score_method.updateScore()
            time_obj.last_day=cur_time
            time_obj.save()
    except:
        makeTimeCheck(cur_time)

    if request.method == "POST":
        handle = request.POST.get('handle')
        if EventParticipants.objects.filter(handle=handle):
            data['error'] = "이미 존재하는 handle입니다."
            return render(request,'baekjoon/event.html', data)
        if api.user_handle_info(handle) is None:
            data['error'] = "존재하지 않는 handle입니다."
            return render(request, 'baekjoon/event.html', data)
        event_object = EventParticipants.objects.create(
            handle=handle,
            score = 0
        )
        event_object.save()
        
        score_method.makeScore(event_object,api.get_problem_info(handle))
    return render(request,'baekjoon/event.html', data)
