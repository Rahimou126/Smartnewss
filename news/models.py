from django.db import models






# Create your models here.



class News(models.Model):
  CHOICES=(
        ('P', 'Politics'),
        ('T', 'Technology'),
        ('S', 'Sport'),
        ('A', 'Art'),
    )





  Title=models.CharField(max_length=10,blank=False,default='Unknown article')
  Photo=models.ImageField(blank=True,default='')
  Source=models.CharField(max_length=10,blank=False,default='')
  Sub_Title=models.CharField(max_length=10,blank=False,default='')
  Content=models.TextField(blank=False,default='')
  Category=models.CharField(max_length=10,choices=CHOICES,blank=False,default='')
