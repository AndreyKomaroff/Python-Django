from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['home', 'blog'] + list(Blog.objects.all())
    
    def location(self, obj):
        if isinstance(obj, str):
            if obj == 'home':
                return reverse('home')
            elif obj == 'blog':
                return reverse('blog')
        else:
            return reverse('post', kwargs={'blog_slug': obj.slug})