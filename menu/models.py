# coding=utf-8
__authors__ = 'renkse, eternalfame'

from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.translation import ugettext_lazy as _

from menu.settings import NAV_MENU_FLATPAGE_MODEL


class Menu(MPTTModel):
    name = models.CharField(_('name'), max_length=255)
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    url = models.CharField(_('url'), max_length=100, blank=True, help_text=_('Example: /page/. This field should be '
                                                                             'filled only if there is no flat page '
                                                                             'associated with this menu instance.'))
    page = models.ForeignKey(NAV_MENU_FLATPAGE_MODEL, blank=True, null=True, related_name='menus',
                             verbose_name=_('flat page'))
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=_('parent menu'))

    class Meta:
        verbose_name = u'меню'
        verbose_name_plural = u'меню'

    def __unicode__(self):
        return self.name

    @property
    def slug(self):
        from warnings import warn
        warn('django_nav_menu.Menu slug attribute is deprecated', PendingDeprecationWarning)
        return self.url

    def get_children(self):
        if hasattr(self, '_cached_children'):
            qs = self._tree_manager.filter(pk__in=[n.pk for n in self._cached_children])
            qs._result_cache = self._cached_children
            return qs
        else:
            if self.is_leaf_node():
                return self._tree_manager.none()
            return self._tree_manager._mptt_filter(parent=self, is_active=True,)

    def save(self, *args, **kwargs):
        # автозаполнение слага пункта меню по урлу из прикрепленной странички
        if self.page:
            self.url = self.page.url
        return super(Menu, self).save(*args, **kwargs)