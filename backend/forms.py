from django import forms
from django.forms import fields
class Info_sysForm(forms.Form):
    name = fields.CharField(label='站点名称')
    descirbe = fields.CharField(label='站点描述')
    keyword= fields.CharField(label='关键字')
    beian = fields.CharField(label='备案号')