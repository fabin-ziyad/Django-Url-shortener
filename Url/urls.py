"""    <!--=====================================
       devopled by fabin ziyad
       github: https://github.com/fabin-ziyad
    ==========================================-->"""
from . import views
from django.urls import path
urlpatterns = [
     path('',views.index,name='home'),
     path('create',views.create,name='create'),
     path('<str:pk>', views.go, name = 'create')
 ]
 