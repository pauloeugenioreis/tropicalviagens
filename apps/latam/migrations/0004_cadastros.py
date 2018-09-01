# Generated by Django 2.1.1 on 2018-09-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latam', '0003_auto_20180831_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastros',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='tx_email', max_length=100, null=True)),
                ('senha', models.CharField(db_column='tx_senha', max_length=20, null=True)),
                ('data_nascimento', models.CharField(db_column='tx_data_nascimento', max_length=20, null=True)),
                ('numero_latam', models.CharField(db_column='tx_numero_latam', max_length=20, null=True)),
                ('nit', models.CharField(db_column='tx_nit', max_length=20, null=True)),
                ('recibo', models.CharField(db_column='tx_recibo', max_length=30, null=True)),
                ('created_at', models.DateField(auto_now_add=True, db_column='dt_solicitacao')),
            ],
            options={
                'db_table': 'cadastros',
                'managed': True,
            },
        ),
    ]