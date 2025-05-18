from django.db import models






# Create your models here.



class News(models.Model):
  
  CHOICES=(
        ('POLITICS','Politics'),
        ('TECHNOLOGY','Technology'),
        ('SPORT','Sport'),
        ('ART','Art'),
    )


  Title=models.CharField(max_length=100,blank=False,default='Unknown article')
  Photo=models.ImageField(blank=True,default='None')
  Source=models.CharField(max_length=100,blank=False,default='')
  Sub_Title=models.CharField(max_length=100,blank=False,default='')
  Content=models.TextField(blank=False,default='')
  Category=models.CharField(max_length=100,choices=CHOICES,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.Title

    

 


