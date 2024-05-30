from rest_framework import serializers
from todolist.models import todolist,dontu
 

class listserializer(serializers.ModelSerializer):
    class Meta:
        model=todolist
        fields='__all__'

class dontuserializer(serializers.ModelSerializer):
    class Meta:
        model=dontu
        fields='__all__'