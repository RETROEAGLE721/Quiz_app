from rest_framework import serializers
from .models import *

class mcqsSerializer(serializers.ModelSerializer):

    class Meta:
        model = mcqs
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'