from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#task və list modelləri yaradılır və konfiqurasiya edirik

class List(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='list',verbose_name='Sahibi:')
    title=models.CharField(max_length=50,verbose_name='Basliq:')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='yaradilma tarixi:')
    confirm = models.BooleanField(default=False,verbose_name='tamamlanilib?:')

    def __str__(self):
        return self.title


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='task',verbose_name='Sahibi:',null=True,blank=True)
    title=models.CharField(max_length=50,verbose_name='basliq:')
    content=models.TextField(verbose_name='mezmun:')
    created_date=models.DateTimeField(auto_now_add=True,verbose_name='yaradilma tarixi:')
    confirm = models.BooleanField(default=False,verbose_name='tamamlanilib?:')
    lists = models.ForeignKey(List, on_delete=models.CASCADE,related_name='task',null=True,blank=True)
    def __str__(self):
        return self.title



