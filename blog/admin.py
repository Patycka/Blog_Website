from django.contrib import admin
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "date")
    list_display = ("title", "author", "date")


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)