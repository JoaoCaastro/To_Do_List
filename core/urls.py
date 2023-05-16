from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),    
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>/', views.update, name='update'),
    path('edit', views.edit, name='edit')

]