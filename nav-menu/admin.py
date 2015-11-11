# coding=utf-8
__authors__ = 'renkse, eternalfame'

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from feincms.admin import tree_editor

from menu.models import Menu

admin.autodiscover()


class MenuAdmin(tree_editor.TreeEditor):
    search_fields = ('name',)
    ordering = ['id', ]
    list_display = ('name', 'is_active',)
    fieldsets = [
        (None,               {'fields': ['name', 'is_active', 'page', 'parent']}),
        (_('URL (if no flat page is selected)'), {'fields': ['url'], 'classes': ['collapse']}),
    ]


admin.site.register(Menu, MenuAdmin)
