from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), 
    path('finches', views.finch_index, name='finches'),
    path('finches/<int:finch_id>/', views.finch_details, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('toys/', views.toys, name='view_toys'),
    path('toys/<int:pk>', views.ToyDetails.as_view(), name='toy_details'),
    path('toys/create/', views.ToyCreate.as_view(), name='add_toy'),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name='toy_delete'),
]