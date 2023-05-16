from django.shortcuts import render, get_object_or_404
from galeria.models import fotografia
from django.http import HttpResponse

# Create your views here.
def index(request):

    fotografias = fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    img = get_object_or_404(fotografia, pk=foto_id)
    print(img.nome)
    return render(request, 'galeria/imagem.html', {"fotografia": img})
