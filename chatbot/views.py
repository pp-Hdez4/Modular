from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ChatPage(request):
    
    return render(request, 'chatbot/chat.html')
    
  
def getResponse(request):
   userMessage = request.GET.get('userMessage')
   return HttpResponse(userMessage)