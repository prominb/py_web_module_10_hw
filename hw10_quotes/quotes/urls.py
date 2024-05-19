from django.urls import path
from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),  # AAAAA
    path('<int:page>', views.main, name='main_paginate'),  # AAAAA
    # NEW START => BEGIN
    path('author/<str:id_>/', views.author_details, name='author_details'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('delete/<int:id_>/', views.delete_quote, name='delete_quote'),
    path('tag/<str:tag>/', views.find_by_tag, name='find_by_tag'),
    # path('tag/<str:tag>/<int:page>', views.find_by_tag, name='tag_paginate'),
]
