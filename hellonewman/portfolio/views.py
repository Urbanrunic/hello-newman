from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from hellonewman.portfolio.models import *


def gallery_home(request):
    """
    displays all published entries in the gallery
        
    """
    works = PortfolioImage.objects.filter(published=True)
    
    return render_to_response("portfolio/index.html", {
        "works": works,
    }, context_instance=RequestContext(request))


def gallery_detail(request, slug):
    """
    Show detailed version of image

    """
    work = get_object_or_404(PortfolioImage, slug=slug, published=True)
    work.increase_read_count()

    return render_to_response("portfolio/detail.html", {
        "work": work,
    }, context_instance=RequestContext(request))


def category_list(request, slug):
    """
    displays all images for the given category
    expects [slug]
    """

    category = get_object_or_404(PortfolioCategory, slug=slug)
    works = PortfolioImage.objects.filter(published=True, category=category)

    return render_to_response("portfolio/index.html", {
        "category": category,
        "works": works,
    }, context_instance=RequestContext(request))
