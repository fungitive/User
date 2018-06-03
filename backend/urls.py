from django.conf.urls import url,include
from backend import views
app_name='backend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index),
    url(r'^sys_info$', views.sys_info),
    url(r'^article_list$', views.article_list),
    url(r'^article_delete$', views.article_delete),
    url(r'^article_edit$', views.article_edit),
    url(r'^article_add$', views.article_add),
    url(r'^article_add1$', views.article_add1),
    url(r'^test$', views.test1),
    url(r'^testimg$', views.testimg),
    url(r'^', include('django.contrib.auth.urls')),
]