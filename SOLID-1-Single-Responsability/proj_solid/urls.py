"""
URL configuration for proj_bd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views.categorias_view import CategoriasView
from app.views.produtos_view import ProdutosView
from app.views.home import Home


from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # define as rotas de URL da nossa aplicacao
    path('', Home.home, name='home'),
    
    # path('instrucoes/', 'instrucoes/instrucoes.html', name='instrucoes'),



    # ===========================================================================
    # Rotas: CATEGORIA
    #   - categorias/              : exibe página de listagem
    #   - categorias/incluir/      : exibe a página de inclusao de registro
    #   - categorias/alterar/<id>/ : exibe a página de alteracao de registro
    #   - categorias/excluir/<id>/ : exibe a página de exclusao de registro
    #   - categorias/salvar/       : insere, altera ou exclui um registro do BD
    # 
    path('categorias/', CategoriasView.listar, name='categorias'),
    path('categorias/incluir/', CategoriasView.incluir, name='categorias_incluir' ), 
    path('categorias/alterar/<int:id>/', CategoriasView.alterar, name='categorias_alterar'),
    path('categorias/excluir/<int:id>/', CategoriasView.excluir, name='categorias_excluir'),

    # ===========================================================================
    # Rotas: PRODUTO
    #   - produtos/              : exibe página de listagem
    #   - produtos/incluir/      : exibe a página de inclusao de registro
    #   - produtos/alterar/<id>/ : exibe a página de alteracao de registro
    #   - produtos/excluir/<id>/ : exibe a página de exclusao de registro
    #   - produtos/salvar/       : insere, altera ou exclui um registro do BD
    # 
    # 
    path('produtos/', ProdutosView.listar, name='produtos'),
    path('produtos/incluir/', ProdutosView.incluir, name='produtos_incluir' ), 
    path('produtos/alterar/<int:id>/', ProdutosView.alterar, name='produtos_alterar'),
    path('produtos/excluir/<int:id>/', ProdutosView.excluir, name='produtos_excluir'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
