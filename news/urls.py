from django.urls import path
from . import views



urlpatterns = [

    path('fetch/',views.fetch,name='fetch'),
    path('news/<int:news_id>/',views.detail,name='detail'),
    

]
