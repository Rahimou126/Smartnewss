
import datetime
from turtle import title

from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404


from .models import News
from django.db.models import Q
from django.http import HttpResponse



# Create your views here.






def fetch(request):

        
        
        search=request.GET.get('search')

        if search:


                news=News.objects.filter(Q(Title__icontains=search) or Q(Content__icontains=search))

                context={'news':news}
        

        else:
                news=News.objects.all().order_by('created_at')
                paginator = Paginator(news, 4)
                page = request.GET.get('page', 1)
                news = paginator.get_page(page)

                context={'news':news}

            
        return render(request,'news/list.html',context)





def detail(request,news_id):

        try:
                

                news_id=get_object_or_404(News, id=news_id)
                
                context={'details':news_id}
        
        except Exception as e:

                HttpResponse("there is now details")
        

        return render(request,'news/detail.html',context)
        
        




        





        
        
                 
















        
        







             
       



        











        
        
        








        

    

    
       
        


    
        
        
    



    
    
    