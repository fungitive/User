from django.contrib import admin
from users.models import User
from .models import Article,Tag,Classify
# Register your models here.

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'username', 'email', 'nickname','date_joined')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-date_joined',)
    # list_editable 设置默认可编辑字段
    list_editable = ['username', 'nickname','date_joined']
    list_filter = ('username','email')
    search_fields = ('username', 'email')  # 搜索字段
    date_hierarchy = 'date_joined'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','create_time','classify','id')

admin.site.register(Article,ArticleAdmin)
#admin.site.register(User,UserAdmin)
admin.site.site_header = '用户管理系统'
admin.site.site_title = '用户管理系统'

admin.site.register(Tag)
admin.site.register(Classify)


