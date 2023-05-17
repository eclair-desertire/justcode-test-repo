from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet,mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer, ProductCardSerializer,UserSerializer, GetUserSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import User, ProductCard
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .permissions import IsCourier


class ProductCardView(GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    permission_classes=[AllowAny]
    serializer_class=ProductCardSerializer
    queryset=ProductCard.objects.all()

class CourierView(ListAPIView):
    permission_classes=[IsCourier] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Поздравляю вы действительно курьер'}, status=status.HTTP_200_OK)

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['title', 'text']

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[AllowAny]
        else:
            self.permission_classes=[IsAdminUser]
        return super(self.__class__, self).get_permissions()


class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenObtainPairSerializer

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenRefreshSerializer

class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes=[AllowAny]
    serializer_class=UserSerializer

class UserView(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=GetUserSerializer
    queryset=User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self,request,*args,**kwargs):
        serializer=self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


def index(request):
    ls=Post.objects.all()
    return render(request,'index.html',{'posts':ls})


def about(request):
    # AboutUs.objects.last()
    # AboutUs.objects.get()
    # AboutUs.objects.filter()
    return render(request,'about.html')

def post_single(request,pk):
    # Post.objects.get(pk=pk)
    p=get_object_or_404(Post.objects.all(),pk=pk)
    return render(request,'post_single.html',{'post':p})

def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('single', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})
# Create your views here.
