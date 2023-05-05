from django.urls import path
from .views import index, about, post_single

urlpatterns=[
    path('',index,name='index'),
    path('<int:pk>/',post_single,name='single'),
    path('about/',about,name='about')
]