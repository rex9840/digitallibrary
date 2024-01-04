from datetime import datetime
from django.core.serializers.json import uuid
from rest_framework import serializers
from .models import *




class UserSerializer(serializers.ModelSerializer): 
    

    #create a private function to generate a uuid for the User
    __id = 0

    ID = serializers.SerializerMethodField('get_id',read_only=True)
    def get_id(self,obj):
        self.id = self.id + 1 
        return self.__id

    DateCreated = serializers.SerializerMethodField('get_date',read_only=True)
    def get_date(self,obj):
        return datetime.now().date().__str__()
    
    UserID = serializers.SerializerMethodField('create_uuid')
    def create_uuid(self,obj):
        id  = self.__id + 1
        date = datetime.now().date().__str__().replace("-","")
        return int(date + str(id))


    class Meta:
        model = User
        fields = ('__all__')
