from django.db import models
import os
import fitz
from django.conf import settings


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
    resource_image = models.ImageField(upload_to=get_resources_filename,null=True, blank=True)
    resource_file = models.FileField(upload_to=get_resource_file_filename, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey("Users",on_delete=models.CASCADE)
    class Meta:
        db_table = "Resources"

    def __str__(self):
        return str(self.resource_id) + " - " + self.name
    
    def extract_image(self):
        BASE_DIR = settings.BASE_DIR 
        file = self.resource_file
        file_path = os.path.join(BASE_DIR,settings.MEDIA_ROOT)+"\\"+str(file).replace("/","\\")

        doc = fitz.open(file_path) 

        first_page = doc[0]

        image_path = os.path.join(BASE_DIR,settings.MEDIA_ROOT)+"\\upload\\resource_image\\"+str(self.resource_id)+"\\" 
        pix = first_page.get_pixmap(matrix=fitz.Identity,dpi=None,colorspace=fitz.csRGB,clip=None,alpha=True,annots=True)

        os.makedirs(image_path,exist_ok=True)
        print(image_path)
        
        pix.save(image_path+"cover_page.png")

        doc.close()

        return "upload/resource_image/"+str(self.resource_id)+"/cover_page.png"    
    

    def save(self,*arg,**kwarg): 
        if self.resource_file and not self.resource_image:
            super(Resources,self).save(*arg,**kwarg)
            image_path =  self.extract_image()
            self.resource_image = image_path
            obj = Resources.objects.get(resource_id=self.resource_id)
            obj.resource_image = image_path 
            obj.save()
        else:
            super(Resources,self).save(*arg,**kwarg) 

