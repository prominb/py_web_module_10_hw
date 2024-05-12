from django.urls import path
from . import views

app_name = 'users'

# urlpatterns = [
#     path('signup/', views.signupuser, name='signup'),
#     path('login/', views.loginuser, name='login'),
#     path('logout/', views.logoutuser, name='logout'),
#     path('profile/', views.profile, name='profile'),
# ]
urlpatterns = [
    path('login/', views.register, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote_author/', views.add_quote, name='add_quote')
]