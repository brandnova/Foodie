from django.shortcuts import render
from .models import SiteSettings

# Create your views here.

def index(request):
    site_settings = SiteSettings.objects.first()  # Assuming there's only one instance
    return render(request, 'core/index.html', {'site_settings': site_settings})
