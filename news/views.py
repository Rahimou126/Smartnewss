
import datetime
from django.shortcuts import render,reverse
from django.template import context

from .models import News
from django.http import Http404, HttpResponse



# Create your views here.






def fetch(request):


        news=News.objects.all().order_by('created_at')
        context={'news':news}

        return render(request,'news/listofnews.html',context)




def search(self,request,search_term):
        if request.method=='GET':

               if self.Title=search_term:
                  filtred_news=News.objects.get(Title=search_term)
               else:
                  Http404('Error')
        return render(request,'news/listofnews.html',filtred_news)
        
                  



        
        
                 
















        
        







             
       



        











        
        
        








        

    

    
       
        


    
        
        
    



    
    
    