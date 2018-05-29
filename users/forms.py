from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User
from django import forms

from django.core.validators import RegexValidator
from django.forms import fields
class RegisterForm(UserCreationForm):
    username = forms.CharField(label='用户名')
    email = forms.EmailField(label='邮箱')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email","nickname",)

    def clean_check_code(self):
        if self.request.session['check_code'].upper() != self.request.POST.get('check_code').upper():
            raise ValidationError(message='验证码错误', code='invalid')

class Info_sysForm(forms.Form):
    name = forms.CharField(label="站点名称")
    descirbe = forms.CharField(label="站点描述")
    keyword= forms.CharField(label="关键字")
    beian = forms.CharField(label="备案号")