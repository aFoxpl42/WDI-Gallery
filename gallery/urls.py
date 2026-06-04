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
    
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name = 'gallery/password_change.html',
        success_url='/password_change/done/'
    ), name='password_change'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'gallery/password_change_done.html',
    ), name = 'password_change_done'),
]
