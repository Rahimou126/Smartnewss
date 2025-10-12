
import datetime
from turtle import title

from django.core.paginator import Paginator
from django.shortcuts import render,reverse
from django.template import context

from .models import News
from django.db.models import Q
from django.http import Http404, HttpResponse



# Create your views here.






def fetch(request):

        news=News.objects.all().order_by('created_at')
        paginator = Paginator(news, 4)

        page = request.GET.get('page', 1)


        news = paginator.get_page(page)
        context={'news':news}

        query=request.GET.get('query')

        if query:

                news=News.objects.filter(Q(Title__icontains=query) or Q(Content__icontains=query))

                context={'news':news}
        else:
                HttpResponse("No news found")


        return render(request,'news/listofnews.html',context)




        
        
                 
















        
        







             
       



        











        
        
        








        

    

    
       
        


    
        
        
    



    
    
    