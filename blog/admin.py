from django.contrib import admin
from .models import Post, User, ProductCard

class PostAdmin(admin.ModelAdmin):
    list_display=('user','title','text','date_post')
    list_filter=('user','date_post')

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(ProductCard)
# Register your models here.
