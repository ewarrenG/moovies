from django.contrib import admin

# Register your models here.

from .models import Blog, BlogAuthor, Movie, Collection
admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(Movie)
admin.site.register(Collection)


