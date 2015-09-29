from django.conf import settings


NAV_MENU_FLATPAGE_MODEL = getattr(settings, "NAV_MENU_FLATPAGE_MODEL", 'django.FlatPage')