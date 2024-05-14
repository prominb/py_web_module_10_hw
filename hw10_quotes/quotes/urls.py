from django.urls import path
from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),  # AAAAA
    path('<int:page>', views.main, name='main_paginate'),  # AAAAA
    # NEW START => BEGIN
    path('author/<str:id_>/', views.author_details, name='author_details'),
]
