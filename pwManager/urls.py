from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('main/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('data_input/',views.data_input,name='data-input'),
    path('delete/<uuid:pk>/',views.delete_cred,name='delete-cred'),

    path('edit/<uuid:pk>/',views.edit_cred,name='edit-cred'),

]
