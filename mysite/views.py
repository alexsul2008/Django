from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .forms import ArticleForm



class HomeListView(ListView):
    model = Articles
    ordering = '-id'
    template_name = 'index.html'
    context_object_name = 'list_articles'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'


def edit_page(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    context = {
        'list_articles': Articles.objects.all().order_by('-id'),
        'form': ArticleForm(),
        'success': success,
    }
    template = 'edit_page.html'
    return render(request, template, context)

def update_page(request, pk):
    success_update = False
    get_article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            success_update = True

    context = {
        'get_article': get_article,
        'update': True,
        'form': ArticleForm(instance=get_article),
        'success_update': success_update
    }
    template = 'edit_page.html'
    return render(request, template, context)


def delete_page(request, pk):
    success_delete = False
    get_article = Articles.objects.get(pk=pk)
    get_article.delete()

    return redirect (reverse('edit_page'))






# def home(request):
#     list_articles = Articles.objects.all()
#     context = {
#         'list_articles': list_articles
#     }
#     template = 'index.html'
#     return render(request, template, context)

# def detail_page(request, id):
#     get_article = Articles.objects.get(id=id)
#     context = {
#         'get_article': get_article
#     }
#     template = 'detail.html'
#     return render(request, template, context)