from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>', views.profile, name='profile'),
    path('search/', views.search_users, name='search-users'),
]
