from django.db import models



class Resources(models.Model):

    def get_profile_pic_filename(self,filename): 
        folder_path = "upload/profile_pic/"+str(self.id)
        return os.path.join(folder_path,filename)

    def get_resource_file_filename(self,filename): 
        folder_path = "upload/resource_file/"+str(self.id)
        return os.path.join(folder_path,filename)
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    Resource_image = models.ImageField(upload_to=get_profile_pic_filename, null=True, blank=True)
    Resource_file = models.FileField(upload_to='upload/resource_file', null=True, blank=True)


    class Meta:
        db_table = "Resources"

    def __str__(self):
        return self.name+ "("+str(self.id)+")"

