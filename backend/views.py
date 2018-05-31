from django.shortcuts import render,redirect,HttpResponse
from users import models
from django.db.models.aggregates import Count
from .forms import *
from .pages import Pagination
# Create your views here.
def logo(request):
    return render(request,'backend/login.html')
def index(request):
    current_page = request.GET.get('page')
    count_pages = models.Article.objects.all().count()
    page_obj = Pagination(count_pages, current_page)
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article_list = models.Article.objects.all().order_by('-create_time')[page_obj.start():page_obj.end()]
    return render(request,'backend/index.html',{'classify_list':classify_list,'article_list':article_list,'page_obj':page_obj})
def sys_info(request):
    sys_info = Info_sysForm()
    return render(request,'backend/sys_info.html',{'sys_info':sys_info})
def article_list(request):
    current_page = request.GET.get('page')
    count_pages = models.Article.objects.all().count()
    page_obj = Pagination(count_pages, current_page)
    article_list = models.Article.objects.all().order_by('-create_time')[page_obj.start():page_obj.end()]
    return render(request,'backend/article_list.html',{'article_list':article_list,'page_obj':page_obj})

def article_edit(request):
    if request.method=="GET":
        nid = request.GET.get('nid')
        obj = models.Article.objects.filter(id=nid).first()
        return render(request, "backend/article_edit.html",{"obj":obj})
    elif request.method=="POST":
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        author = request.POST.get('author')
        models.Article.objects.filter(id=nid).update(id=nid,title=title,author=author)
        return redirect("/article_list")
    return

def article_add(request):
    if request.method=="GET":
        classify = models.Classify.objects.all()
        tags = models.Tag.objects.all()
        return render(request,'backend/article_add.html',{'classify':classify,'tags':tags})
    elif request.method=="POST":
        title = request.POST.get('title')
        return redirect("/article_list")
def article_delete(request):
    nid = request.GET.get('nid')
    models.Article.objects.filter(id=nid).delete()
    return redirect(to='article_list')

