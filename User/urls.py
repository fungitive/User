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
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from users.models import Classify
from django.views.static import serve


# sitemaps = {
#     'users': GenericSitemap({'queryset': Classify.objects.all(), 'date_field': 'pub_date'}, priority=0.6),
#     # 如果还要加其它的可以模仿上面的
# }
app_name = 'users'
urlpatterns = [
    url(r'^adm/', admin.site.urls),
    url(r'^backend/', include('backend.urls')),
    url(r'^header.html', views.header),
    url(r'^article', views.article, name='article'),
    url(r'^list_summary.html', views.list_summary),
    url(r'^list_classify.html$', views.list_classify),
    url(r'^list_tag.html$', views.list_tag),
    url(r'^search.html$', views.search),
    url(r'^list_date-(?P<ctime>\w+-*\w*).html$', views.list_data),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^index.html$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', views.upload_image, name='upload_image'),
    url(r'^backend/upload/(?P<dir_name>[^/]+)$', views.upload_image, name='upload_image'),
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^upload/artilce/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]


