from django.contrib import admin
from django.db.models import get_model
from imagekit.admin import AdminThumbnail

class PortfolioCategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)

class PortfolioImageAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = ('title', 'admin_thumbnail', 'published', 'created_on')
    list_filter = ('published',)
    save_on_top = True
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

admin.site.register(get_model('portfolio', 'portfoliocategory'), PortfolioCategoryAdmin)
admin.site.register(get_model('portfolio', 'portfolioimage'), PortfolioImageAdmin)

