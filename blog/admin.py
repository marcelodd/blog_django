from django.contrib import admin
from models import Category, Post

class AutoSlug(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category)
admin.site.register(Post,AutoSlug)