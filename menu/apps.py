# coding=utf-8
try:
    from django.apps import AppConfig
except ImportError:
    pass
else:
    class MenuConfig(AppConfig):
        name = u"menu"
        label = u"menu"
        verbose_name = u"Меню"