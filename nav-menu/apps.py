# coding=utf-8
__author__ = "eternalfame"

try:
    from django.apps import AppConfig
except ImportError:
    pass
else:
    from django.utils.translation import ugettext_lazy as _

    class MenuConfig(AppConfig):
        name = u"nav-menu"
        label = u"menu"
        verbose_name = _(u"menu")