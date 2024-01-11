from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .roles import Role

class UserMananger(BaseUserManager): 
    def create_user(self, email,name,password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be defined")
        email = self.normalize_email(email)
        user = self.model(Email = email , Name = name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, role_id=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, name, password, role_id, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    
    ID = models.IntegerField(primary_key=True,help_text="Auto Incremented ID for the user")
    DateCreated = models.DateTimeField(auto_now_add=True,help_text="Date of creation of the user")
    UserID = models.IntegerField(unique=True,help_text="Unique User ID assogned to user for ideentifiacations")
    Name = models.CharField(max_length=50 , help_text="Name of the user") 
    Email = models.EmailField(unique=True,help_text="Email of the user")
    Password = models.CharField(help_text=" Password of the user") 
    Address = models.CharField(max_length=50, help_text="Address of the user") 
    Role_id = models.ForeignKey(Role,on_delete=models.SET_NULL ,null=True , default = 2 , help_text="Role and perms of the user as defined from ROLE table BY DEAFULT= 2 [STUDENT]") 


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

    
    objects = UserMananger()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Name']

    def __str__(self) -> str:
       return '{'+'\t'+f'ID\t->{self.ID}|\tUserID\t->{self.UserID}|\tName\t->{self.Name}|\tEmail\t->{self.Email}|\tRole_id\t->{self.Role_id.pk}'+'\t}'






