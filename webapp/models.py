import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField("title",max_length=200)
    text = models.TextField("main sentence...")
    date = models.DateTimeField("date", default=timezone.now)

    def __str__(self):
        return self.title

class Schedule(models.Model):
    '''スケジュール'''
    summary = models.CharField('概要',max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時刻', default=datetime.time(7,0,0,))
    end_time = models.TimeField('終了時刻', default=datetime.time(7,0,0))
    date = models.DateField('日付') 
    create_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.summary