import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
# xxxField 确定数据类型
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )    
    # def was_published_recently(self):
    #     # 检查问题是否是在过去的 24 小时内发布， 大于等于的情况下返回 True
    #     #  datetime.timedelta(days=1) 表示时间段，为 1 天
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # ForeignKey 定义相互之间关系， 这里每个选择都对应一个问题。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text