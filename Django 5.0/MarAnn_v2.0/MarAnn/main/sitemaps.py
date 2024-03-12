from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['home', 'blog']
    
    def location(self, obj):
        return reverse(obj)
