from django.shortcuts import render
from .forms import coordinacionForm
# Create your views here.


def coordinacionView(request):
    data = {
        'form' : coordinacionForm()
    }
    
    return render(request, 'adminprofile/registrarcoord.html', data)