from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app.forms.produto_form import ProdutoForm
from app.repositories.produtos_repository import ProdutosRepository as pr

class ProdutosView:
    def listar(request):
        try:
            registros = pr.listar()
            return render(request, 'produtos_listar.html', context={'registros': registros})
        except Exception as err:
                return render(request, 'home.html', context={'ERRO': err})

    def incluir(request):
        try:
            if request.POST:
                form = request.POST
                pr.incluir(form)
                return HttpResponseRedirect(reverse("produtos")) 
            return render(request, 'produtos_editar.html', context={'acao': 'Inclusão', 'form': ProdutoForm()})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})

    def alterar(request, id):
        try:
            if request.POST:
                form = request.POST
                pr.alterar(form)
                return HttpResponseRedirect(reverse("produtos"))
            registro = pr.buscar_por_id(id)
            return render(request, 'produtos_editar.html', context={'acao': 'Alteração', 'form': ProdutoForm(initial=registro)})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})
    
    def excluir(request, id):
        try:
            if request.POST:
                pr.excluir(id)
                return HttpResponseRedirect(reverse("produtos"))
            registro = pr.buscar_por_id(id)
            return render(request, 'produtos_editar.html', context={'acao': 'Exclusão', 'form': ProdutoForm(initial=registro)})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})