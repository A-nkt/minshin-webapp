from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text="facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="twiiter URL")
    youtube = models.URLField(blank=True, null=True, help_text="youtube URL")
    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="SocialMediaSettings")
    ]
