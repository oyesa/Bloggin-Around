from django.contrib import admin

from blogapp.models import Blogpost, Comments, Likes

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Comments)
admin.site.register(Likes)

