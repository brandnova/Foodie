from django.db import models

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200)
    site_description = models.TextField( default='Welcome to my site')
    favicon = models.ImageField(upload_to='site_settings/')
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255)
    background_video = models.FileField(upload_to='site_settings/', blank=True, null=True)

    def __str__(self):
        return self.site_title
