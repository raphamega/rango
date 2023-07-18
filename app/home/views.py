from django.shortcuts import render
from .forms import ContactForm
from .models import Pag_Contato


# Create your views here.

def home_page(request):
    tela = "home/index.html"

    return render(request, tela)


def about_page(request):
    tela = "home/view.html"
    context = {
        'title': "Kinquilharias RCM",
        'titulo': "Sobre",
        'comentario': "Um pouco sobre nós",
    }
    return render(request, tela, context)


def contact_page(request):
    tela = "home/view.html"
    form = ContactForm(request.POST or None)
    context = {
        'title': "Kinquilharias RCM",
        'titulo': "Contato",
        'comentario': "Deixe aqui suas criticas, comentarios e sujestões ou duvidas",
        'form': form,
    }

    if form.is_valid():
        contato = Pag_Contato(
            nome=request.POST.get("nome_completo"),
            email=request.POST.get("email"),
            mensagem=request.POST.get("mensagem"),

        )
        contato.save()
        context = {
            'title':"Contact Page",
            'comentario':"Mensagem enviada com sucesso",
        }
        return render(request, tela, context)
    return render(request, tela, context)
