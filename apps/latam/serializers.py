from rest_framework import serializers

from apps.latam.models import Computer, Cadastros


class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = '__all__'

class CadastrosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cadastros
        fields = '__all__'
