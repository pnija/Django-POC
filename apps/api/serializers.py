from rest_framework import serializers
from apps.api.models import Animal, Herd, AnimalWeight

class AnimalWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalWeight
        exclude = []

class AnimalWeightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalWeight
        exclude = ['id', 'animals']

class AnimalSerializer(serializers.ModelSerializer):
    weights = AnimalWeightListSerializer(source='get_animal', many=True)
    class Meta:
        model = Animal
        exclude = []


class AnimalListSerializer(serializers.ModelSerializer):
    weights = AnimalWeightListSerializer(source='get_animal', many=True)
    class Meta:
        model = Animal
        exclude = ['id',]