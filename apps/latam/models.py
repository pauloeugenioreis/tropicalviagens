from django.db import models

# Create your models here.
class ModelBase(models.Model):
    created_at = models.DateField(
        db_column='dt_cadastro',
        auto_now_add=True,
    )

    class Meta:
        abstract = True

class Computer(ModelBase):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=244, null=True, db_column='tx_nome_computador')

    class Meta:
        managed = True
        db_table = 'computadores'