from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from django.db.models import Q

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published = True,
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def category(request,category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        is_published = True,
        category__id = category_id
    ))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title_category': f'{recipes[0].category.name} - category'
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published = True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'is_detail_page': True,
        'recipe': recipe
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term)
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes
    })