from django.contrib.sitemaps import Sitemap
from hellonewman.blog.models import Entry
from hellonewman.portfolio.models import PortfolioImage

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Entry.objects.published()

    def lastmod(self, obj):
        return obj.updated_on


class PortfolioSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return PortfolioImage.objects.filter(published=True)

    def lastmod(self,obj):
        return obj.updated_on
