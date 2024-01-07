from django.db import models
import uuid
from datetime import datetime
from api.Models import example
from django.contrib import admin 



class Role(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=50)
    Description = models.CharField(max_length=50,blank=True ,help_text = 'Description of the role and its permisions')
    class Meta:
        db_table = "Role"
        db_table_comment = "Role and Permissions Table"
    
    def __str__(self) -> str:
        return "{"+f"RoleID : {self.RoleID} | RoleName : {self.RoleName}" +"}"
class User(models.Model):
    
    # data fields for the models (attributes or columns of tables )
    ID = models.IntegerField(primary_key=True,help_text="Auto Incremented ID for the user")
    DateCreated = models.DateTimeField(auto_now_add=True,help_text="Date of creation of the user")
    UserID = models.IntegerField(help_text="Unique User ID assogned to user for ideentifiacations")
    Name = models.CharField(max_length=50 , help_text="Name of the user") 
    Email = models.EmailField(help_text="Email of the user")
    Password = models.CharField(help_text=" Password of the user") 
    Address = models.CharField(max_length=50, help_text="Address of the user") 
    Role_id = models.ForeignKey(Role,on_delete=models.SET_NULL ,null=True , default = 2 , help_text="Role and perms of the user as defined from ROLE table BY DEAFULT= 2 [STUDENT]") 

    class Meta:
        db_table = "Users" # table name in the database 
        db_table_comment = "Reegistered User  information Table"
        ordering = ['DateCreated']
    
    def display_role(self):
        return self.Role_id.RoleID 
    display_role.short_description = 'RoleID'
    
    def display_Rolename(self):
        return self.Role_id.RoleName
    display_Rolename.short_description = 'RollName'
    
    def save(self, *args, **kwargs):
        if not self.ID:
            if User.objects.last() is None:
                self.ID = 1
            self.ID = User.objects.last().ID + 1
        if not self.UserID:
            date = datetime.now().date().__str__().replace('-', '')
            uuid = date+"0"+str(self.ID)
            self.UserID = int(uuid)
 
        super(User, self).save(*args, **kwargs)


    def __str__(self) -> str:
       return '{'+'\t'+f'ID\t➡️{self.ID}|\tUserID\t➡️{self.UserID}|\tName\t➡️{self.Name}|\tEmail\t➡️{self.Email}|\tRole_id\t➡️{self.Role_id.pk}'+'\t}'





