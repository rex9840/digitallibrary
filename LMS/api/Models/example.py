from django.db import models



class ExampleMolde(models.Model): 
    ExampleField = models.CharField(max_length=50)
    class Meta:
        db_table = "ExampleTable"
        db_table_comment = "ExampleTable"


