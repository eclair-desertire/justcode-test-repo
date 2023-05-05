from django.shortcuts import render, get_object_or_404
from blog.models import Post


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
# Create your views here.
