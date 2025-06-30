from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "total_participants" : 3,
    }
    return render(request,'baekjoon/event.html', data)
