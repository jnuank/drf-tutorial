from django.contrib import admin

from .models import Book


class BookModelAdmin(admin.ModelAdmin):
    """
    オプションで、管理サイトで登録・編集が
    できるようなやつ
    """
    list_display = ('title', 'price', 'id', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')

admin.site.register(Book, BookModelAdmin)