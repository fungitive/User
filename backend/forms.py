from django import forms
class Info_sysForm(forms.Form):
    name = forms.CharField(label="站点名称")
    descirbe = forms.CharField(label="站点描述")
    keyword= forms.CharField(label="关键字")
    beian = forms.CharField(label="备案号")