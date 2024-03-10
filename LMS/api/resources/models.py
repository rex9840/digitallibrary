from django.db import models
import os

class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Tags"
    def __str__(self): 
        return self.tag_name


class Resources(models.Model):

    def get_resources_filename(self,filename): 
        folder_path = "upload/resource_image/"+str(self.resource_id)
        return os.path.join(folder_path,filename)

    def get_resource_file_filename(self,filename): 
        folder_path = "upload/resource_file/"+str(self.resource_id)
        return os.path.join(folder_path,filename)
    
    resource_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tags,blank=True)
    resource_image = models.ImageField(upload_to=get_resources_filename,
                                       default='upload/resource_image/default_book.png',null=True, blank=True)
    resource_file = models.FileField(upload_to=get_resource_file_filename, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey("Users",on_delete=models.CASCADE)
    class Meta:
        db_table = "Resources"

    def __str__(self):
        return str(self.resource_id) + " - " + self.name

