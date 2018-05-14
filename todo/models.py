from django.db import models
from django.contrib.auth.models import User
# (1對多)
class Tag(models.Model):
    title = models.CharField(max_length=255,unique=True)

    # 回傳值
    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField('標題',max_length=255)
    content = models.CharField('內容',max_length=500)
    status = models.BooleanField('已完成',default=False)
    tags = models.ManyToManyField(Tag,verbose_name='標籤')
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='建立者')


    # 回傳值
    def __str__(self):
        return self.title
