from django.contrib import admin
from django.db.models import get_model
from imagekit.admin import AdminThumbnail

class PortfolioCategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)

class PortfolioImageAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = ('title', 'admin_thumbnail', 'published', 'created_on', 'order', 'read_count')
    list_filter = ('published',)
    save_on_top = True
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_editable = ('order',)

    class Media:
        js = [
            '/static/js/sortable_list.js'
        ]
    

admin.site.register(get_model('portfolio', 'portfoliocategory'), PortfolioCategoryAdmin)
admin.site.register(get_model('portfolio', 'portfolioimage'), PortfolioImageAdmin)

