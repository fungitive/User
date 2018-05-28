from django.shortcuts import render,redirect,HttpResponse
from django.db.models.aggregates import Count
from users import models
# Create your views here.
from .forms import RegisterForm

def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')

    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})
def index(request):
    from users.pages import Pagination
    current_page = request.GET.get('page')
    count_pages = models.Article.objects.all().count()
    page_obj = Pagination(count_pages, current_page)
    article_list = models.Article.objects.all().order_by('-create_time')[page_obj.start():page_obj.end()]
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'index.html',{
                    'article_list':article_list,
                    'tag_list':tag_list,
                    'classify_list':classify_list,
                    'date_list':date_list,
                    'page_obj':page_obj}
                  )

def article(request):
    nid = request.GET.get('nid')
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article = models.Article.objects.filter(id = nid).first()
    article_list = models.Article.objects.all().order_by('-create_time')
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return  render(request,'article.html',{'article':article,'classify_list': classify_list,
                                           'article_list': article_list,
                                           'tag_list': tag_list,
                                           'date_list': date_list
                                           })

def header(request):
    return render(request, 'include/header.html')

def list_summary(request):
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article_list = models.Article.objects.all().order_by('-create_time')
    article = models.Article.objects.all()[1::5]
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'list_summary.html', {'classify_list': classify_list,
                                            'article_list': article_list,
                                            'tag_list': tag_list,
                                            'date_list': date_list,

                                            })

def list_tag(request):
    nid = request.GET.get('nid')
    article = models.Article.objects.filter(tag=nid).first()
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article_list = models.Article.objects.filter(tag=nid).all().order_by('-create_time')
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'list_classify.html', {'classify_list': classify_list,
                                                 'article_list': article_list,
                                                 'tag_list': tag_list,
                                                 'date_list': date_list,
                                                 'article': article,
                                                  })

def list_classify(request):
    nid = request.GET.get('nid')
    article = models.Article.objects.all()[1:5]
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article_list = models.Article.objects.filter(classify=nid).all().order_by('-create_time')
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'list_classify.html', {'classify_list': classify_list,
                                                 'article_list': article_list,
                                                 'tag_list': tag_list,
                                                 'date_list': date_list,
                                                 'article': article,
                                                  })


def list_data(request,ctime):
    nid = request.GET.get('nid')
    article = models.Article.objects.all()[1:5]
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    article_list = models.Article.objects.extra(where=['strftime("%%Y-%%m",update_time)=%s'], params=[ctime, ]).all().order_by('-create_time')
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'list_classify.html', {'classify_list': classify_list,
                                                 'article_list': article_list,
                                                 'tag_list': tag_list,
                                                 'date_list': date_list,
                                                 'article': article,
                                                  })

def search(resquest):
    keywords = resquest.POST.get('keywords')
    print(keywords)
    result = models.Article.objects.filter(title=keywords)
    return render(resquest,'search.html',{'result':result})
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import json
import datetime as dt
import uuid
@csrf_exempt
def upload_image(request, dir_name):
    ##################
    #  kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("imgFile", None)
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")


# 目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    url_part = dir_name + '/%d/%d/' % (today.year, today.month)
    dir_name = os.path.join(dir_name, str(today.year), str(today.month))
    print("*********", os.path.join(settings.MEDIA_ROOT, dir_name))
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, dir_name)):
        os.makedirs(os.path.join(settings.MEDIA_ROOT, dir_name))
    return dir_name,url_part


# 图片上传
def image_upload(files, dir_name):
    # 允许上传文件类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    relative_path_file, url_part = upload_generation_dir(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    print("&&&&path", path)
    if not os.path.exists(path):  # 如果目录不存在创建目录
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url =settings.MEDIA_URL + url_part +file_name
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}
