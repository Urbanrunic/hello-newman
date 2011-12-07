from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

tagging = models.get_app('tagging')

class People(models.Model):
    """
    Base class for linking to people I respect.
    """

    name = models.CharField(_('name'), max_length=250) 
    url = models.URLField(verify_exists=True, max_length=200, null=False, blank=False)
    published = models.BooleanField(_('Published'), default=True)
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()
    
    class Meta:
        ordering = ['name', ]
        verbose_name_plural = "people"

    def __unicode__(self):
        return self.name
