import os

from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range, make_pagination


# Create your views here.

PER_PAGES = int(os.environ.get('PER_PAGE', 6))

def home(request):
    recipes = Recipe.objects.filter(
        is_published = True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })

def category(request,category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        is_published = True,
        category__id = category_id
    ))

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)


    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
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

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)


    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })