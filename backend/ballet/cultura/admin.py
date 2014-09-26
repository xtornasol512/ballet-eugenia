from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from cultura.models import Post


class AdminPosts(SummernoteModelAdmin):
	model = Post


admin.site.register(Post, AdminPosts)