from django.shortcuts import render

# Create your views here.

def ChatPage(request):
    
    return render(request, 'chatbot/chat.html')
    
  
