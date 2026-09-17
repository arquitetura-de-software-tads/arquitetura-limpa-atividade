from django import forms
from app.repositories.categorias_repository import CategoriasRepository as cr

class ProdutoForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    categoria_id = forms.ChoiceField(label='Categoria', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categorias = cr.listar()
        self.fields['categoria_id'].choices = categorias