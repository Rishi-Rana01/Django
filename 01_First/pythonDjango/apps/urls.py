
from django.urls import path
from . import views

urlpatterns = [
   path('', views.all, name='all'),
   path('app_stores/', views.app_store_view,name='app_stores')
]

