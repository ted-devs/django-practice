from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
import re


# Create your views here.


def home(request):
    return HttpResponse('Hello, Django!')


def hello_there(request, name):
    print(request.build_absolute_uri()) # optional

    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
