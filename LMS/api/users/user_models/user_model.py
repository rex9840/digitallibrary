from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
import os

class UserManager(BaseUserManager):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.id_instance = 0

    def id_count(self):
        if Users.objects.last():
            self.id_instance = Users.objects.last().ID
        self.id_instance += 1
        return self.id_instance


    def create_user(self,email,first_name,last_name,age,address,phone_number,school_id,is_teacher:bool=False,password=None): 
        if  not email: 
            raise ValueError("User must have an email address")
        if not phone_number:
            raise ValueError("User must have a phone number")
        if not school_id:
            raise ValueError("User must have a school id")

        user = self.model(
            ID = self.id_count(),
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name, 
            age = age, 
            address = address, 
            phone_number = phone_number, 
            school_id = school_id,
            is_teacher = is_teacher,
            is_active = True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,first_name,last_name,age,address,phone_number,school_id,password=None): 
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name, 
            age = age, 
            address = address, 
            phone_number = phone_number, 
            school_id = school_id,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Users(AbstractBaseUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.id_instance = 0

    def get_profile_pic_filename(self,filename): 
        folder_path = str(self.school_id)
        return os.path.join(folder_path,filename)

    ID= models.IntegerField()
    password = models.CharField(verbose_name="password")
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    email = models.EmailField(verbose_name="email",unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    school_id = models.IntegerField(primary_key=True)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=get_profile_pic_filename,blank=True)


    USERNAME_FIELD = 'school_id'
    REQUIRED_FIELDS = ['email','first_name','last_name','age','address','phone_number','password']
    PASSWORD_FIELD = 'password'
    
    @property
    def id(self): 
        return self.school_id


    def __str__(self):
       full_name =  f'{self.first_name}' +" " + f'{self.last_name}'
       if self.is_admin:
           return full_name + " (Admin)"
       if self.is_teacher:
           return full_name + " (Teacher)"
       return full_name + " (Student)"

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        ordering = ['date_joined']

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    def id_count(self):
        if Users.objects.last():
            self.id_instance = Users.objects.last().ID
        self.id_instance += 1
        return self.id_instance

    def save(self,*args,**kwargs):
        if not self.ID:
            self.ID = self.id_count()
        self.set_password(self.password)
        super().save(*args,**kwargs)   
