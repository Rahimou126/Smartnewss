
import datetime
from turtle import title

from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404

from .models import News
from django.db.models import Q
from django.http import HttpResponse



# Create your views here.
  
     
        
def fetch(request):
    
    search = request.GET.get('search', '').strip()

    
    news_queryset = News.objects.all().order_by('-created_at')

    
    if search:
        news_queryset = news_queryset.filter(
            Q(Title__icontains=search) | Q(Content__icontains=search)
        )

    
    paginator = Paginator(news_queryset, 4)  
    page_number = request.GET.get('page', 1)
    news_page = paginator.get_page(page_number)

    
    context = {
        'news': news_page,
        'search': search,
    }

    return render(request, 'news/list.html', context)





        
        




        





        
        
                 
















        
        







             
       



        











        
        
        








        

    

    
       
        


    
        
        
    



    
    
    