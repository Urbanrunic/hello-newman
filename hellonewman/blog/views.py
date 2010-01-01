from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import date_based, list_detail

from django.contrib.sites.models import Site

from hellonewman.blog.models import Entry, Distraction, Blog
from hellonewman.blog.exceptions import InvalidBlog

def filter_blog(request, slug=None):
    """
    segregates the blog by blog type
    expects a slug in the url to set the session.
    this may change to cookie based session in the future
    but for now we will set it in the session

    if no slug is passed then the user wants to see all
    journal types.
    """

    if slug is None:
        try:
            del request.session['blog_filter']
        except KeyError:
            pass
    else:
        request.session['blog_filter'] = slug

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    

def home_page(request):
    """
    Displays the landing page
    If the blog filter is set in the session then only show
    those kind of entries
    """
    
    if 'blog_filter' in request.session:
        entries = Entry.objects.filter(blog__slug=request.session['blog_filter'])
    else:
        entries = Entry.objects.all()[:9]
                                 
    distractions = Distraction.objects.all()[:5]
    
    return render_to_response('blog/home_page.html', {
        "entries": entries,
        "distractions": distractions,
    }, context_instance=RequestContext(request))

def entry_detail(request, year, month, day, slug, **kwargs):
    """
    displays the details of an ``Entry``.
        
    """
    entry = get_object_or_404(Entry, slug=slug)
    entry.increase_read_count()

    return render_to_response("blog/entry_detail.html", {
        "entry": entry,
    }, context_instance=RequestContext(request))


def archive_index(request):
    """
    """
    return date_based.archive_index(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_month(request):
    """
    A wrapper around ``django.views.generic.date_based.archive_month`` that
    displays an archive of entries for the given month.
    
    """
    return date_based.archive_month(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_year(request):
    """
    A wrapper around ``django.views.generic.date_based.archive_year`` that
    displays an archive of entries for the given year.
    
    """
    return date_based.archive_year(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        make_object_list=True,
        template_object_name='entry'
    )

def blog_feed(request, blog=None):
    """
    Atom Feeds.  Borrowed and modified from
    http://github.com/eldarion/biblion
    """
    
    try:
        entries = Entry.objects.blog(blog)
    except InvalidBlog:
        raise Http404()
    
    if blog is None:
        blog = "combined"
    
    feed_title = "Journal: %s" % (blog[0].upper())
    
    current_site = Site.objects.get_current()
    blog_url = "http://%s%s" % (current_site.domain, reverse("home-page"))
    
    if section == "combined":
        url_name = "blog-feed-combined"
        kwargs = {}
    else:
        url_name = "blog-feed"
        kwargs = {"journal": blog}
    feed_url = "http://%s%s" % (current_site.domain, reverse(url_name, kwargs=kwargs))
    
    if entries:
        feed_updated = posts[0].published
    else:
        feed_updated = datetime(2010, 1, 1, 0, 0, 0)
    
    # create a feed hit
    hit = FeedHit()
    hit.request_data = serialize_request(request)
    hit.save()
    
    atom = render_to_string("blog/atom_feed.xml", {
        "feed_id": feed_url,
        "feed_title": feed_title,
        "blog_url": blog_url,
        "feed_url": feed_url,
        "feed_updated": feed_updated,
        "entries": entries,
        "current_site": current_site,
    })
    return HttpResponse(atom, mimetype="application/atom+xml")
 
