from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from core.sitemap import BlogSitemap, PortfolioSitemap

admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
    'portfolio': PortfolioSitemap,
        }

urlpatterns = patterns('',
    #url(r'^$', redirect_to, {'url': 'http://gregnewman.org/journal/'}),
    url(r'^$', 'portfolio.views.home', name='home'),
    (r'^journal/', include('blog.urls')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    (r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    #legacy urls
    (r'^blog/text/13432767/mjd-painting$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/oct/10/faces-nfl-project-mjd/'}),
    (r'^blog/text/13427726$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/sep/13/faces-nfl-project-drew-brees/'}),
    (r'^blog/text/13427725$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/sep/13/faces-nfl-project-tom-brady/'}),
    (r'^blog/text/13427722/bill-cosby$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/sep/13/bill-cosby/'}),
    (r'^blog/text/13393337/self-portrait-caricature-painting$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/apr/13/self-portrait-caricature-painting/'}),
    (r'^blog/text/13393339/ozan-value-study$', redirect_to, {'url': 'http://gregnewman.org/journal/2011/feb/16/ozan-value-study/'}),
    (r'^blog/text/13393357/python-illustration$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/nov/2/python-illustration/'}),
    (r'^blog/text/13393358/chimp-study$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/oct/19/chimp-study/'}),
    (r'^blog/text/13393359/ram-sketch$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/oct/6/ram-sketch/'}),
    (r'^blog/text/13393360/stork-lost-one-adoption-renunion$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/jun/11/stork-lost-one-adoption-reunion/'}),
    (r'^blog/text/13393361/rent-to-own$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/jan/17/rent-to-own/'}),
    (r'^blog/text/13393363/painterly-portrait-processing$', redirect_to, {'url': 'http://gregnewman.org/journal/2010/jan/3/painterly-portrait-processing/'}),
)
