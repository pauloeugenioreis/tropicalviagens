from django.db import models

# Create your models here.
class ModelBase(models.Model):
    created_at = models.DateTimeField(
        db_column='dt_cadastro',
        auto_now_add=True,
    )

    class Meta:
        abstract = True

class Computer(ModelBase):
    id = models.BigAutoField(primary_key=True)
    programa = models.CharField(max_length=244, null=True, db_column='tx_programa')
    name = models.CharField(max_length=244, null=True, db_column='tx_nome_computador')

    class Meta:
        managed = True
        db_table = 'computadores'


class Cadastros(ModelBase):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100, null=True, db_column='tx_email')
    senha = models.CharField(max_length=20, null=True, db_column='tx_senha')
    data_nascimento = models.CharField(max_length=20, null=True, db_column='tx_data_nascimento')
    numero_latam = models.CharField(max_length=20, null=True, db_column='tx_numero_latam')
    nit = models.CharField(max_length=20, null=True, db_column='tx_nit')
    recibo = models.CharField(max_length=30, null=True, db_column='tx_recibo')


    class Meta:
        managed = True
        db_table = 'cadastros'

