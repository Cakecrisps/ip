from django.shortcuts import render,HttpResponse
from mainkal.models import PostCategory,Post
# Create your views here.
def index(request):
    context = {"is_login":False,'username':'sosunok','lvl':'LVL-666',"posts":Post.objects.all()}
    for i in Post.objects.all():
        print(i.author,i.desc,i.img)
    return render(request,'main/index.html',context)
def profile(request):
    return render(request,'main/profile.html',{'username':'sosunok','lvl':'LVL-666','about':"An HTTP 304 not modified status code means that the website you're requesting hasn't been updated since the last time you accessed it. Typically, your browser will save (or cache) web pages so it doesn't have to repeatedly download the same information. This is an attempt to speed up page delivery."})
def login(request):
    return render(request,'main/login.html')
def reg(request):
    return render(request,'main/reg.html')
