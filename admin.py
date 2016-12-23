from django.contrib import admin
from .models import Image_User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'number')
    list_filter = ('user',)
    search_fields = ['image']

admin.site.register(Image_User, PostAdmin)