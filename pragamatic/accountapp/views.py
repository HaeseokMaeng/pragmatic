from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from .models import HelloWorld


def Hello(request) :

    if request.method == "POST" :
        temp = request.POST.get('hello_world_input')

        tmp_HelloWorld = HelloWorld()
        tmp_HelloWorld.text = temp
        tmp_HelloWorld.save()
        # return render(request, 'accountapp/hello_world.html', context={"text": 'POST METHOD !!!', "hello_world_list" : hello_world_list, })
        return HttpResponseRedirect(reverse_lazy('account:hello'))
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={"text": 'GET METHOD !!!', "hello_world_list" : hello_world_list,})
