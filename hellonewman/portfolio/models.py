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
    description = models.TextField(_('description'), blank=True)
    category = models.ManyToManyField(PortfolioCategory)
    original_image = models.ImageField(upload_to='portfolio')
    thumbnail = ImageSpec([resize.Crop(125, 125)],
        image_field='original_image',
        format='JPEG', options={'quality': 100})

    order = models.PositiveIntegerField(_('order'), default=1, blank=True)

    # flags
    published = models.BooleanField(_('Published'), default=True)
    
    # datefields
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()


    class Meta:
        ordering = ['-created_on', ]
        verbose_name_plural = 'Portfolio Images'
        
    def __unicode__(self):
        return self.title




