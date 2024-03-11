from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer): #implementing serializer to render data into JSON format
    class Meta:
        model=Data
        fields=('name', 'description')