from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators  import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)

class HelloView(APIView):
   def get(self, request):
      try:
         logger.info('Calling http')
         response = requests.get('https://httpbin.org/delay/2')
         logger.info('Received the response')
         data = response.json()
      except request.ConnectionError:
         logger.critical('httpbin offline')

      return render(request, 'hello.html', {'name':'Mosh'})