from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import HelloWorld


def Hello(request) :

    if request.method == "POST" :
        temp = request.POST.get('hello_world_input')

        tmp_HelloWorld = HelloWorld()
        tmp_HelloWorld.text = temp
        tmp_HelloWorld.save()

        return render(request, 'accountapp/hello_world.html', context={"hello_world" : tmp_HelloWorld, })
    else :
        return render(request, 'accountapp/hello_world.html', context={"text": 'GET METHOD !!!', })
