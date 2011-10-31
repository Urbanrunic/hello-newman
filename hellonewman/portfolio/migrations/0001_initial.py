# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PortfolioCategory'
        db.create_table('portfolio_portfoliocategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='name', overwrite=False, db_index=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('portfolio', ['PortfolioCategory'])

        # Adding model 'PortfolioImage'
        db.create_table('portfolio_portfolioimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('original_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('portfolio', ['PortfolioImage'])

        # Adding M2M table for field category on 'PortfolioImage'
        db.create_table('portfolio_portfolioimage_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioimage', models.ForeignKey(orm['portfolio.portfolioimage'], null=False)),
            ('portfoliocategory', models.ForeignKey(orm['portfolio.portfoliocategory'], null=False))
        ))
        db.create_unique('portfolio_portfolioimage_category', ['portfolioimage_id', 'portfoliocategory_id'])


    def backwards(self, orm):
        
        # Deleting model 'PortfolioCategory'
        db.delete_table('portfolio_portfoliocategory')

        # Deleting model 'PortfolioImage'
        db.delete_table('portfolio_portfolioimage')

        # Removing M2M table for field category on 'PortfolioImage'
        db.delete_table('portfolio_portfolioimage_category')


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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
