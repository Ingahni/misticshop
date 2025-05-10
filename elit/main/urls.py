from django.urls import path
from . import views

# создаем urls 
app_name = 'main'

urlpatterns = [
    # путь для отображения главной страницы
    path('', views.popular_list, name='popular_list'),
    # пцть для отображения каталога
    path('shop/', views.product_list, name='product_list'),
    # пкть для фильтрации по категориям
    path('shop/<slug:slug>/', views.product_detail,
         name='product_detail'), 
    
    path('shop/category/<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
]
