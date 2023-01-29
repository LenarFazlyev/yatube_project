from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'template': template,
    }
    return render(request, template, context)
    #return HttpResponse('Главная страница')


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'template': template,
        'slug': slug,
    }
    return render(request, template, context)
    #return HttpResponse(f"Посты отфильтрованные по группам {slug}")