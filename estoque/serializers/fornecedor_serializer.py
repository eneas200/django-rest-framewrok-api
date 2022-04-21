# ~/estoque.fornecedor_serializer.py
from rest_framework import serializers

from estoque.models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fornecedor 
		fields = [
			'id',
			'nomeContato',
			'empresa',
			'email',
			'telefoneFixo',
		]
 