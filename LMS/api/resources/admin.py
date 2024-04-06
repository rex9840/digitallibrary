from django.contrib import admin
from .models import Tags, Resources

# Register your models here.


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag_id','tag_name']
    list_filter =['tag_id','tag_name']



@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin): 
    list_display = ['resource_id','name','description','tags_list','resource_image','resource_file','created_at','uploaded_by'] 
    exclude = ["resource_id"]
    list_filter = ['name','tags','created_at','uploaded_by']
    
    def tags_list(self, obj):
        return "\n".join([tag.tag_name for tag in obj.tags.all()])
    tags_list.short_description = 'Tags'
