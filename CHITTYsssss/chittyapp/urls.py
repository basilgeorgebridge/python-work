from django.urls import path
from chittyapp import admin_views
from chittyapp import user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('',admin_views.login, name='login'),
path('adminindex/',admin_views.adminindex, name='adminindex'),
path('userindex/',admin_views.userindex, name='userindex'),
path('members/add/',admin_views.add_members, name='add-members'),
path('members/view/',admin_views.view_members, name='view-members'),
path('members/detailedview/<str:pk>/',admin_views.detailed_view_members, name='detailed-view-members'),
path('members/edit/<str:pk>/',admin_views.edit_members, name='edit-members'),
path('logout', admin_views.logout,name ='logout'),
path('change-password/',
        auth_views.PasswordChangeView.as_view(template_name='admin/change-password.html',
        success_url = '/adminindex/'
        ),name='change-password'),
path('user-change-password/',
        auth_views.PasswordChangeView.as_view(template_name='admin/change-user-password.html',
        success_url = '/adminindex/'
        ),name='change-user-password'),

]