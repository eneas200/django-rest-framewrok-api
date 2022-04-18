# Generated by Django 4.0.4 on 2022-04-18 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeContato', models.CharField(max_length=150)),
                ('empresa', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=200)),
                ('telefoneFixo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('perfilFuncionario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('codigoIdentificacao', models.CharField(max_length=20)),
                ('dataFabricacao', models.CharField(max_length=20)),
                ('dataVencimento', models.CharField(max_length=20)),
                ('valor_unitario', models.FloatField()),
                ('fornecedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEstoque', models.DateField()),
                ('totalEstoque', models.IntegerField()),
                ('totalLimit', models.IntegerField()),
                ('descricao', models.TextField()),
                ('funcionario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.funcionario')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]
