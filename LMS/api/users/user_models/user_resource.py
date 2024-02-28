from django.db import models
from django.core.validators import MaxValueValidator

class UserResourceInteraction(models.Model):
    user_id = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_id')
    resource_id = models.ForeignKey('Resources', models.DO_NOTHING, db_column='resource_id')
    Rating = models.IntegerField(validators=[MaxValueValidator(5)],default=0)
    Comment = models.CharField(max_length=500, null=True, blank=True)
    Downloaded = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    class Meta:
        db_table = "UserResourceInteraction"



