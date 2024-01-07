from datetime import datetime
from rest_framework import serializers
from .models import User  # Assuming your User model is in the same app

class UserSerializer(serializers.ModelSerializer):
    
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.id_instance = 0
#
#    def get_uid(self):
#        if User.objects.last():
#            self.id_instance = User.objects.last().ID
#        self.id_instance += 1
#        date = datetime.now().date().__str__().replace('-', '')
#        uuid = date+"0"+str(self.id_instance)
#        return int(uuid)
    
    ID = serializers.IntegerField(required=False)
    UserID = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'
#
#    def create(self, validated_data):
#        validated_data['UserID'] = self.get_uid()
#        validated_data['ID'] = self.id_instance
#        return super().create(validated_data)
#
