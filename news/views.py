
from django.shortcuts import render,reverse
from django.template import context

from .models import News
from django.http import HttpResponse



# Create your views here.



def fetch(request):


        news=News.objects.all().order_by('created_at')
        context={'news':news}

        return render(request,'news/listofnews.html',context)



        

    

    
       
        


    
        
        
    



    
    
    