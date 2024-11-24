from django.urls import path
from .views import index , trainer



urlpatterns =[
    path('',index ,  name='index'),
    path('trainer',trainer ,  name='tariner')
    
    
    ]