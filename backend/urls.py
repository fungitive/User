from django.conf.urls import url,include
from backend import views
urlpatterns = [
    url(r'^$', views.logo, name='logo'),
    url(r'^index.html$', views.index),
    url(r'^sys_info$', views.sys_info),
    url(r'^article_list$', views.article_list),
    url(r'^article_edit$', views.article_edit),
    url(r'^article_add$', views.article_add),

]