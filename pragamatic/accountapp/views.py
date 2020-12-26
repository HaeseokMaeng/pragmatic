from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from .models import HelloWorld


def Hello(request) :

    if request.method == "POST" :
        temp = request.POST.get('hello_world_input')

        tmp_HelloWorld = HelloWorld()
        tmp_HelloWorld.text = temp
        tmp_HelloWorld.save()
        return HttpResponseRedirect(reverse('account:hello'))
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={"text": 'GET METHOD !!!', "hello_world_list" : hello_world_list,})


class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'