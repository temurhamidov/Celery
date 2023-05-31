from django.shortcuts import render
from django.http import HttpResponse
from .tasks import slow_func
# Create your views here.



def index(request):
    slow_func.delay(123438)
    return HttpResponse('Site is working')
