from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    nickname = models.CharField('昵称',max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length=32,)
    author = models.CharField(verbose_name='作者',max_length=12)
    summary = models.CharField(verbose_name='摘要', max_length=100)
    img = models.ImageField(verbose_name='缩略图',upload_to="./article/",
                            help_text="大小200*200，不超过200k",
                            default="/upload/article/common.jpg",
                            auto_created=True,
                            null=True,blank=True)
    content = models.TextField(verbose_name='内容', max_length=9999)
    tag = models.ManyToManyField('Tag',verbose_name='标签')
    classify = models.ForeignKey('Classify',verbose_name='分类')
    create_time = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间')

    class Meta:
        db_table = 'article'
        verbose_name_plural = '全部文章'
    def __str__(self):
        return self.title
class Tag(models.Model):
    name = models.CharField(verbose_name='名称',max_length=12)
    class Meta:
        db_table = 'tag'
        verbose_name_plural = '文章标签'
    def __str__(self):
        return self.name

class Classify(models.Model):
    name = models.CharField(verbose_name='名称',max_length=12)
    class Meta:
        db_table = 'classify'
        verbose_name_plural = '文章分类'
    def __str__(self):
        return self.name