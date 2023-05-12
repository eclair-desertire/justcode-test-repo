from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, about, post_single, post_form, TokenObtainPairView, TokenRefreshView, RegisterView, UserView, PostView


router=DefaultRouter()
router.register('post',PostView,basename='post')

urlpatterns=[
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView.as_view({'post':'create'})),
    path('user/me/',UserView.as_view({'get':'get_current_user'})),
    path('',index,name='index'),
    path('<int:pk>/',post_single,name='single'),
    path('post/new/',post_form,name="post_form"),
    path('about/',about,name='about'),
    path('api/',include(router.urls))
]