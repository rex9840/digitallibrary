from django.db import models
from django.core.validators import MaxValueValidator

class UserResourceInteraction(models.Model):
    user_id = models.ForeignKey('Users', models.CASCADE, db_column='user_id')
    resource_id = models.ForeignKey('Resources', models.CASCADE, db_column='resource_id')
    rating = models.FloatField(validators=[MaxValueValidator(5)],default=0)
    class Meta:
        db_table = "UserResourceInteraction" 
    def __str__(self):
        return str(self.user_id) + " - " + str(self.resource_id)


