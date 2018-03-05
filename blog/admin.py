from django.contrib import admin
from .models import Bookmark, Member

class BookmarkAdmin(admin.ModelAdmin):
    list_display=('title','url')

admin.site.register(Bookmark, BookmarkAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name')

admin.site.register(Member, MemberAdmin)