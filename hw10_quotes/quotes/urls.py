from django.urls import path

from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('author/<str:author>/', views.AuthorView.as_view(), name='author'),
    path('tag/<str:tag>/', views.QuotesByTagView.as_view(), name='quotes_by_tag'),
    # path('tag/<int:pk>/', views.QuotesByTagView.as_view(), name='quotes_by_tag'),
]
