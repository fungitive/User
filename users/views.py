from django.shortcuts import render,redirect
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
    article_list = models.Article.objects.all()
    tag_list = models.Tag.objects.annotate(num_article=Count('article'))
    classify_list = models.Classify.objects.annotate(num_article=Count('article'))
    date_list = models.Article.objects.raw(
        'select id, count(id) as num,strftime("%Y-%m",update_time) as ctime from article group by strftime("%Y-%m",update_time)')
    return render(request, 'index.html',{
                    'article_list':article_list,
                    'tag_list':tag_list,
                    'classify_list':classify_list,
                    'date_list':date_list}
                  )

def article(request):
    nid = request.GET.get('nid')
    article = models.Article.objects.filter(id = nid).first()
    return  render(request,'article.html',{'article':article})