from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

from imagekit.models import ImageSpec
from imagekit.processors import resize


class PortfolioCategory(models.Model):
    """
    Base class to segregate the types of portfolios
    """

    name = models.CharField(_('name'), max_length=100)
    slug = AutoSlugField(populate_from='name')

    # flags
    published = models.BooleanField(_('Published'), default=True)

    # datefields
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()

    class Meta:
        ordering = ['-created_on', ]
        verbose_name_plural = 'Portfolio Categories'
        
    def __unicode__(self):
        return self.name

class PortfolioImage(models.Model):
    """
    Base class to manage porfolio images and their assignment to
    the categories [PortfolioCategory]
    """

    title = models.CharField(_('title'), max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(_('description'), blank=True)
    category = models.ManyToManyField(PortfolioCategory)
    original_image = models.ImageField(upload_to='portfolio')
    thumbnail = ImageSpec([resize.Crop(125, 125)],
        image_field='original_image',
        format='JPEG')
    #', options={'quality': 100}

    buy_link = models.URLField(verify_exists=True, max_length=200, null=True, blank=True)

    meta_title = models.CharField(_('Meta Title'), max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)
    meta_description = models.TextField(_('Meta Description'), null=True, blank=True)

    # relations
    related_content = models.ManyToManyField("self", null=True, blank=True)

    order = models.PositiveIntegerField(_('order'), default=1, blank=True)

    # flags
    published = models.BooleanField(_('Published'), default=True)
    read_count = models.IntegerField(default=0, editable=False)
    
    # datefields
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()

    # increase read count
    def increase_read_count(self):
        self.read_count += 1
        self.save()

    class Meta:
        ordering = ['-created_on', ]
        verbose_name_plural = 'Portfolio Images'
        
    def __unicode__(self):
        return self.title




