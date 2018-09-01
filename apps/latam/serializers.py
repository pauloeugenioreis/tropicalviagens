from rest_framework import serializers

from apps.latam.models import Computer


class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = '__all__'
