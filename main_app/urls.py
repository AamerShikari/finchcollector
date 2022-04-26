from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), 
    path('finches', views.finch_index, name='finches'),
    path('finches/<int:finch_id>/', views.finch_details, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:finch_id>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:finch_id>/delete', views.FinchDelete.as_view(), name='finch_delete'),
]