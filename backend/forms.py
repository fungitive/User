
from django import  forms
from django.forms import fields
from users.models import *
import datetime
from django.forms import widgets
import django.utils.timezone as timezone
from django.forms import ModelChoiceField


class Info_sysForm(forms.Form):
    name = fields.CharField(label='站点名称')
    descirbe = fields.CharField(label="站点描述")
    keyword= fields.CharField(label="关键字")
    beian = fields.CharField(label="备案号")

class ArticleForm(forms.Form):
    title = fields.CharField(label='标题',max_length=40,
                             error_messages={
                                 'required':'标题不能为空',
                                 'max_length':'长度不能超过20个字'
                             },
                             widget=widgets.TextInput(attrs={'class': "form-control",'placeholder':"标题",'size':"60"})
                             )
    author = fields.CharField(label='作者',max_length=12,
                              error_messages={
                                  'required': '作者不能为空',
                                  'max_length': '长度不能超过6个字'
                              },
                              widget=widgets.TextInput(attrs={'class': "form-control",'placeholder':"作者"}))
    summary = fields.CharField(label='摘要',max_length=200,
                               error_messages={
                                   'required': '摘要不能为空',
                                   'max_length': '长度不能超过100个字'
                               },
                               widget=widgets.Textarea(attrs={'row':"2",'style':"height:60px;",'class': "form-control",'placeholder':"摘要不要超过100字"}))
    img = fields.FileField(label='缩略图',required=True)
    content = fields.CharField(label='内容',
                               error_messages={
                                   'required': '文章内容不能为空',
                               },
                                widget=widgets.Textarea(attrs={'class': "form-control",'id': "kindeditor"}))
    tag = forms.ModelMultipleChoiceField(label='标签',queryset=Tag.objects.all(),
                                 error_messages={
                                     'required': '请选择标签',
                                 },
                                 widget=widgets.SelectMultiple(attrs={'class': "form-control"}))
    classify = forms.ModelChoiceField(label='分类',queryset=Classify.objects.all(),
                                      error_messages={
                                          'required': '请选择分类',
                                      },
                                      widget=widgets.Select(attrs={'class': "form-control"}))
