from datetime import datetime 
from rest_framework import serializers
from api.users.__models__.user import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_instance = 0
   
    def get_uid(self):
        if User.objects.last():
            self.id_instance = User.objects.last().ID
        self.id_instance += 1
        date = datetime.now().date().__str__().replace('-', '')
        uuid = date+"0"+str(self.id_instance)
        return int(uuid)
    
    ID = serializers.IntegerField(required=False)
    UserID = serializers.IntegerField(required=False)
    Password = serializers.CharField(required=True, max_length=16,min_length=8)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['UserID'] = self.get_uid()
        validated_data['ID'] = self.id_instance
        validated_data['Password'] = make_password(validated_data['Password'])

        return super().create(validated_data)
    
