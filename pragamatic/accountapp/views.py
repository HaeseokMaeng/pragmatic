from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .decorators import account_ownership_required
from .forms import AccountUpdateForm
from .models import HelloWorld

has_ownership = [login_required, account_ownership_required]

@login_required
def Hello(request) :

    if request.method == "POST" :
        temp = request.POST.get('hello_world_input')

        tmp_HelloWorld = HelloWorld()
        tmp_HelloWorld.text = temp
        tmp_HelloWorld.save()
        return HttpResponseRedirect(reverse('accountapp:hello'))
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={"text": 'GET METHOD !!!', "hello_world_list" : hello_world_list,})


class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/create.html'


@method_decorator(has_ownership, name='get')
class AccountDetailView(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView) :
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

