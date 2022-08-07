from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipe/search/', search, name='search'),
    path('recipes/category/<int:category_id>/', category, name='category'),
    path('recipes/<int:id>/', recipe, name='recipe'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)