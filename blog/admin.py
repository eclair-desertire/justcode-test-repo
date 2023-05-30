from django.contrib import admin
from .models import Post, User, ProductCard



admin.site.register(Post)

class PostInline(admin.StackedInline):
    model=Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','role']
    inlines=[PostInline]

admin.site.register(ProductCard)
# Register your models here.
