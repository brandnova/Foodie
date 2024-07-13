from django.db import models

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200)
    site_description = models.TextField( default='Welcome to my site')
    favicon = models.ImageField(upload_to='site_settings/')
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255)
    background_video = models.FileField(upload_to='site_settings/', blank=True, null=True)
    authPage_bgImg= models.ImageField(upload_to='site_settings/', null=True)
    site_logo= models.ImageField(upload_to='site_settings/', null=True, blank=True)
    support_email = models.EmailField(null=True)
    contact_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    open_hrs = models.CharField(max_length=255, null=True, blank=True)
    live_chat_wgt = models.CharField(max_length=1000, null=True, blank=True)
    whatsapp_btn = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.site_title
