from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from cultura.models import Post, Tag


class AdminPosts(SummernoteModelAdmin):
    model = Post
    filter_horizontal =('tags',)


admin.site.register(Post, AdminPosts)
admin.site.register(Tag)