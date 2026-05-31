from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'home_page'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/add/', views.add_artwork, name='add_artwork'),
    path('dashboard/edit/<int:pk>/', views.edit_artwork, name='edit_artwork'),
    path('dashboard/delete/<int:pk>/', views.delete_artwork, name='delete_artwork'),
    
]
