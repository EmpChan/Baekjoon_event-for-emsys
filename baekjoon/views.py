from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        handle = request.POST.handle
        
    data = {
        'total_participants' : '',
    }
    return render(request,'baekjoon/event.html', data)
