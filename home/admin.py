from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post, Comment, Vote

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    search_fields = ('post_title', 'body')
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('post_title',)}
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Vote)
