"""User URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from users import views


app_name = 'users'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^header.html', views.header),
    url(r'^article', views.article, name='article'),
    url(r'^list_summary.html', views.list_summary),
    url(r'^list_classify.html$', views.list_classify),
    url(r'^list_tag.html$', views.list_tag),
    url(r'^search.html$', views.search),
    url(r'^list_date-(?P<ctime>\w+-*\w*).html$', views.list_data),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index')
]


