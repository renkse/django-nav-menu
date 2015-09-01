# coding=utf-8
__author__ = 'renkse'

from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class Menu(MPTTModel):
    name = models.CharField(_('name'), max_length=255)
    is_active = models.BooleanField(verbose_name='активное', default=True)
    slug = models.CharField(_('slug'), max_length=100, blank=True, help_text='Заполняйте это поле только в том случае,'
                                                                             ' если для данного пункта меню не '
                                                                             'выбрана информационная страница (например /page/).')
    page = models.ForeignKey(FlatPage, blank=True, null=True, related_name='page',
                             verbose_name='простая страница')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='родительское меню')

    class Meta:
        verbose_name = u'меню'
        verbose_name_plural = u'меню'

    def __unicode__(self):
        return self.name

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
            self.slug = self.page.url
        return super(Menu, self).save(*args, **kwargs)