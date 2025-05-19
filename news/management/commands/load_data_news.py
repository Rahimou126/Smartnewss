from sys import stdout
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
  


  def handle(self,*args,**kwargs):
      
      try:
          
          call_command('loaddata','news.json')
          self.stdout.write(self.style.SUCCESS('sucesseffuly import data from fixtures to database'))

      except Exception as e:
          
          self.stdout.write(self.style.ERROR('error loading data'))



