from django.contrib import admin
from news import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','user','status','created']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','status']

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.City)
admin.site.register(models.Post,PostAdmin)
