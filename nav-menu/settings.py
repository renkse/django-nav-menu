from django.conf import settings

__author__ = "eternalfame"


NAV_MENU_FLATPAGE_MODEL = getattr(settings, "NAV_MENU_FLATPAGE_MODEL", 'flatpages.FlatPage')