from django.shortcuts import render,redirect,HttpResponse
from users.models import *
from django import forms
import os
from django.forms import fields
from django.db.models.aggregates import Count
from backend.forms import *
from .pages import Pagination
# Create your views here.
def login(request):
    return render(request,'backend/login.html')
def index(request):
    current_page = request.GET.get('page')
    count_pages = Article.objects.all().count()
    page_obj = Pagination(count_pages, current_page)
    classify_list = Classify.objects.annotate(num_article=Count('article'))
    article_list = Article.objects.all().order_by('-create_time')[page_obj.start():page_obj.end()]
    return render(request,'backend/index.html',{'classify_list':classify_list,'article_list':article_list,'page_obj':page_obj})
def sys_info(request):
    sys_info = Info_sysForm()
    return render(request,'backend/sys_info.html',{'sys_info':sys_info})
def article_list(request):
    current_page = request.GET.get('page')
    count_pages = Article.objects.all().count()
    page_obj = Pagination(count_pages, current_page)
    article_list = Article.objects.all().order_by('-create_time')[page_obj.start():page_obj.end()]
    return render(request,'backend/article_list.html',{'article_list':article_list,'page_obj':page_obj})

def article_edit(request):
    if request.method=="GET":
        nid = request.GET.get('nid')
        print(nid)
        article = Article.objects.filter(id=nid).first()
        tags = article.tag.all()
        print(tags)
        return render(request,'backend/article_edit.html',{'article':article,'tag':tags})
    elif request.method=="POST":
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        author = request.POST.get('author')
        Article.objects.filter(id=nid).update(id=nid,title=title,author=author)
        return redirect("/article_list")


def article_add(request):
    if request.method=="GET":
        classify = Classify.objects.all()
        tags = Tag.objects.all()
        return render(request,'backend/article_add.html',{'classify':classify,'tags':tags})
    elif request.method=="POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        summary = request.POST.get('summary')
        img = request.FILES.get('img')
        content = request.POST.get('content')
        tag = request.POST.getlist('tag')
        classify = request.POST.get('classify')
        article = Article.objects.create(title=title,author=author,summary=summary,
                                         classify_id=classify,content=content,img=img,create_time=None,update_time=None)
        print(article.id)
        for i in tag:
            article.tag.add(i)
            return redirect('/backend/article_list')
        print(tag)
        print(classify)
        #Article.objects.create(title=title,author=author,summary=summary,classify_id=classify.id)
        return redirect('/')


def article_delete(request):
    nid = request.GET.get('nid')
    article_obj=Article.objects.filter(id=nid).delete()
    return redirect('/backend/article_list')

def article_add1(request):
    if  request.method=="POST":
        import time
        obj = ArticleForm(request.POST, request.FILES)
        if obj.is_valid():
            tag_id = Tag.objects.filter(name=obj.cleaned_data['author']).first()
            # img = obj.cleaned_data['img']
            # time = time.strftime('%Y%m%d%H%M%S')
            # ext = os.path.splitext(img.name)[1]
            # img.name = time + ext
            # title = obj.cleaned_data['title']
            # author = obj.cleaned_data['author']
            # tag = obj.cleaned_data['author']
            # classify = obj.cleaned_data['classify']
            # content = obj.cleaned_data['content']
            # summary = obj.cleaned_data['summary']
            print(tag_id)
            return redirect('/')
    else:
        obj = ArticleForm()
        return render(request, 'backend/article_add1.html', {'form': obj})

def test1(request):
    return render(request, "backend/test.html")

class TestimgForm(forms.Form):
    title = fields.CharField()
    img = fields.FileField()
    times = fields.DateTimeField(widget=widgets.DateTimeInput(attrs={'type':"datetime-local",'value':"2018-09-01-14:02:30"}
                                                                ))
def testimg(request):
    import time
    if request.method == 'GET':
        img = TestimgForm()
        return render(request, 'backend/testimg.html',{'img':img})
    else:
        obj = TestimgForm(request.POST, request.FILES)
        if obj.is_valid():
        #(request.FILES['file'])
            # title = request.FILES.get('title')
            # img = request.FILES.get('img')
            title = obj.cleaned_data['title']
            times = obj.cleaned_data['times']
            img = obj.cleaned_data['img']
            time = time.strftime('%Y%m%d%H%M%S')
            ext = os.path.splitext(img.name)[1]
            img.name = time + ext
            #重命名
            times1=datetime.datetime.now()
            print(times1)
            # Imgtest.objects.create(title=title,img=img)
            # img是对象（文件大小，文件名称,文件内容。。。）
            # file_path = os.path.join('upload/article',time+ext)
            file_path = os.path.join('upload/article', img.name)
            f = open(file_path,'wb')
            for line in img.chunks():
                f.write(line)
            f.close()
            return HttpResponse('...')

