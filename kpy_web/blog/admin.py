from django.contrib import admin
from .models import Post, Comment

# override lại lớp kế thừa để tùy biến cho Admin 
class CommentInLine(admin.StackedInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_at']
    search_fields = ['title']
    inlines = [CommentInLine]
admin.site.register(Post, PostAdmin)
