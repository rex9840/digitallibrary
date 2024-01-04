from datetime import datetime
from django.core.serializers.json import uuid
from rest_framework import serializers
from .models import *




class UserSerializer(serializers.ModelSerializer): 
    
    #create a private function to generate a uuid for the User
    __id = User.objects.count()

    ID = serializers.IntegerField(read_only=True)
    def __create_uuid(self):
        id  = self.__id + 1
        date = datetime.now().date().__str__().replace("-","")
        return int(date + str(id))

    UserID = serializers.SerializerMethodField('_create_uuid')
    class Meta:
        model = User
        fields = '__all__'
