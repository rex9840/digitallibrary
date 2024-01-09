from django.db import models



class Role(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=50)
    Description = models.CharField(max_length=50,blank=True ,help_text = 'Description of the role and its permisions')
    class Meta:
        db_table = "Role"
        db_table_comment = "Role and Permissions Table"
    
    def __str__(self) -> str:
        return "{"+f"RoleID : {self.RoleID} | RoleName : {self.RoleName}" +"}"
