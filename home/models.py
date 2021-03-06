from __future__ import absolute_import, unicode_literals

from datetime import datetime

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.search import index


class HomePage(Page):
    pass


class SinglePage(Page):
    date = models.DateTimeField("Post date", default=datetime.now)
    subtitle = models.CharField(max_length=250, blank=True)
    header_image = models.ForeignKey('wagtailimages.Image',
                                     on_delete=models.SET_NULL, related_name='+', blank=True, null=True,)

    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('subtitle'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('header_image'),
    ]


class MenuItem(Page):
    external_link = models.URLField(blank=True)
    menu_icon = models.ForeignKey('wagtailimages.Image',
                                  on_delete=models.SET_NULL, related_name='+', blank=True, null=True,)

    content_panels = Page.content_panels + [
        FieldPanel('external_link'),
        ImageChooserPanel('menu_icon'),
    ]
