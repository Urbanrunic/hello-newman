# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PortfolioImage.slug'
        db.add_column('portfolio_portfolioimage', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, default='', populate_from='title', overwrite=False, db_index=True), keep_default=False)

        # Adding field 'PortfolioImage.keywords'
        db.add_column('portfolio_portfolioimage', 'keywords', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Changing field 'PortfolioImage.description'
        db.alter_column('portfolio_portfolioimage', 'description', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'PortfolioImage.slug'
        db.delete_column('portfolio_portfolioimage', 'slug')

        # Deleting field 'PortfolioImage.keywords'
        db.delete_column('portfolio_portfolioimage', 'keywords')

        # Changing field 'PortfolioImage.description'
        db.alter_column('portfolio_portfolioimage', 'description', self.gf('django.db.models.fields.TextField')(default=''))


    models = {
        'portfolio.portfoliocategory': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'PortfolioCategory'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False', 'db_index': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'portfolio.portfolioimage': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'PortfolioImage'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.PortfolioCategory']", 'symmetrical': 'False'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'blank': 'True'}),
            'original_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'read_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
