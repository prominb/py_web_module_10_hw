from django.urls import path
from . import views


app_name = 'quotes'

urlpatterns = [
    # path('', views.main, name='main'),  # AAAAA
    # path('tag/', views.tag, name='tag'),
    # path('note/', views.note, name='note'),
    # path('detail/<int:note_id>/', views.detail, name='detail'),
    # path('done/<int:note_id>', views.set_done, name='set_done'),
    # path('<int:page>', views.main, name='main_paginate'),  # AAAAA
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:quotes_id>/', views.detail, name='detail'),
]
