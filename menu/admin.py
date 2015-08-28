# coding=utf-8
__author__ = 'renkse'

from django.contrib import admin
from models import Menu
from feincms.admin import tree_editor

admin.autodiscover()


class MenuAdmin(tree_editor.TreeEditor):
    search_fields = ('name',)
    ordering = ['id', ]
    list_display = ('name', 'is_active',)
    fieldsets = [
        (None,               {'fields': ['name', 'is_active', 'page', 'parent']}),
        ('Ссылка (если не выбрана информационная страница)', {'fields': ['slug'], 'classes': ['collapse']}),
    ]


admin.site.register(Menu, MenuAdmin)