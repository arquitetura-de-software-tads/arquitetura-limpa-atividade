from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app.repositories.categorias_repository import CategoriasRepository
from app.forms.categoria_form import CategoriaForm

class CategoriasView:
    def listar(request):
        try:
            registros = CategoriasRepository.listar()
            return render(request, 'categorias_listar.html', context={'registros': registros})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})

    def incluir(request):
        try:
            if request.POST:
                form = request.POST
                CategoriasRepository.incluir(form['descricao'])
                return HttpResponseRedirect(reverse("categorias")) 
            return render(request, 'categorias_editar.html', context={'acao': 'Inclusão', 'form': CategoriaForm()})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})

    def alterar(request, id):
        try:
            if request.POST:
                form = request.POST
                CategoriasRepository.alterar(id, form['descricao'])
                return HttpResponseRedirect(reverse("categorias"))
            registro = CategoriasRepository.buscar_por_id(id)
            return render(request, 'categorias_editar.html', context={'acao': 'Alteração', 'form': CategoriaForm(initial=registro)})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})
       
    def excluir(request, id):
        try:
            if request.POST:
                CategoriasRepository.excluir(id)
                return HttpResponseRedirect(reverse("categorias"))
            registro = CategoriasRepository.buscar_por_id(id)
            return render(request, 'categorias_editar.html', context={'acao': 'Exclusão', 'form': CategoriaForm(initial=registro)})
        except Exception as err:
            return render(request, 'home.html', context={'ERRO': err})