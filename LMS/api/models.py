from django.db import models
import uuid
from datetime import datetime


class Role(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=50)
    Description = models.CharField(max_length=50,blank=True ,help_text = 'Description of the role and its permisions')
    class Meta:
        db_table = "Role"
        db_table_comment = "Role and Permissions Table"
    
    def __str__(self) -> str:
        return str(self.RoleID) +"::" + str(self.RoleName)

class User(models.Model):
    
    # data fields for the models (attributes or columns of tables )
    ID = models.AutoField(primary_key=True,help_text="Auto Incremented ID for the user")
    DateCreated = models.DateTimeField(auto_now_add=True,help_text="Date of creation of the user")
    UserID = models.IntegerField(unique=True,help_text="Unique ID for the user",editable=False)
    Name = models.CharField(max_length=50 , help_text="Name of the user") 
    Email = models.EmailField(help_text="Email of the user")
    Password = models.CharField(help_text=" Password of the user") 
    Address = models.CharField(max_length=50, help_text="Address of the user") 
    Role_id = models.ForeignKey(Role,on_delete=models.SET_NULL ,null=True , default = 2 , help_text="Role and perms of the user as defined from ROLE table BY DEAFULT= 2 [STUDENT]") 

    class Meta:
        db_table = "Users" # table name in the database 
        db_table_comment = "Reegistered User  information Table"
        ordering = ['DateCreated']
    
    def __str__(self) -> str:
        return str(self.UserID) +"::" + str(self.Name) + "::" + str(self.Role_id)








