import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
from .decorators import article_ownership_required
from .forms import ArticleCreationForm
from .models import Article, Favorite


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView) :
    model = Article
    form_class = ArticleCreationForm
    # success_url = ''
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tmp_article_id = self.kwargs.get('pk')
        tmp_user = self.request.user

        context['favorite_checked'] = Favorite.objects.filter(writer=tmp_user, article=tmp_article_id)
        context['favorite_count'] = Favorite.objects.filter(article=tmp_article_id).count()

        return context

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView) :
    model = Article
    form_class = ArticleCreationForm
    # success_url = ''
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView) :
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:list')


class ArticleListView(ListView) :
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5


def article_favorite(request) :

    target_article_pk = request.POST.get('target_article_pk', None)  # ajax 통신을 통해서 template에서 POST방식으로 전달
    user = request.user
    favorite_item = Favorite.objects.filter(writer=user, article=target_article_pk)

    main_status = 1
    tmp_sub_status = -1
    if favorite_item.exists():
        favorite_item.delete()
        tmp_sub_status = 2
        tmp_message = "Favorite Unheck success"
    else:
        tmp_article = Article.objects.get(pk=target_article_pk)
        Favorite(writer=user, article=tmp_article).save()
        tmp_sub_status = 1
        tmp_message = "Favorite heck success"

    item_cnt = Favorite.objects.filter(article=target_article_pk).count()
    context = {
        'status': 1,
        'sub_status': tmp_sub_status,
        'favorite_count': item_cnt,
        'message': tmp_message
    }

    return HttpResponse(json.dumps(context), content_type="application/json")
    #return JsonResponse(context, status=200)

class FavoriteView(View) :
    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            tmp_article_id = request.POST['target_article_pk']

            user = self.request.user
            favorite_item = Favorite.objects.filter(article=tmp_article_id)

            tmp_sub_status = -1
            if favorite_item.exists():
                favorite_item.delete()
                tmp_sub_status = 2
                tmp_message = "Favorite Unheck success"
            else:
                Favorite(user=user, article=tmp_article_id).save()
                tmp_sub_status = 1
                tmp_message = "Favorite heck success"

            item_cnt = Favorite.objects.filter(article=tmp_article_id).count()
            return JsonResponse({'status': 1, 'sub_status': tmp_sub_status, 'message': tmp_message, "Total": item_cnt }, status=200)
        else :
            return JsonResponse({'status' : -1, 'message':'The CONTENT_TYPE is not application/json' }, status=200)

