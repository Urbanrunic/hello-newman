# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False, db_index=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('blog', ['Blog'])

        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
        ))
        db.send_create_signal('blog', ['Category'])

        # Adding model 'Entry'
        db.create_table('blog_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('markup', self.gf('django_markup.fields.MarkupField')(default='textile', max_length=255)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expire_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('read_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('blog', ['Entry'])

        # Adding M2M table for field related_content on 'Entry'
        db.create_table('blog_entry_related_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('to_entry', models.ForeignKey(orm['blog.entry'], null=False))
        ))
        db.create_unique('blog_entry_related_content', ['from_entry_id', 'to_entry_id'])

        # Adding M2M table for field category on 'Entry'
        db.create_table('blog_entry_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('category', models.ForeignKey(orm['blog.category'], null=False))
        ))
        db.create_unique('blog_entry_category', ['entry_id', 'category_id'])

        # Adding M2M table for field blog on 'Entry'
        db.create_table('blog_entry_blog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('blog', models.ForeignKey(orm['blog.blog'], null=False))
        ))
        db.create_unique('blog_entry_blog', ['entry_id', 'blog_id'])

        # Adding model 'Distraction'
        db.create_table('blog_distraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expire_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('blog', ['Distraction'])

        # Adding model 'FeedHit'
        db.create_table('blog_feedhit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_data', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('blog', ['FeedHit'])


    def backwards(self, orm):
        
        # Deleting model 'Blog'
        db.delete_table('blog_blog')

        # Deleting model 'Category'
        db.delete_table('blog_category')

        # Deleting model 'Entry'
        db.delete_table('blog_entry')

        # Removing M2M table for field related_content on 'Entry'
        db.delete_table('blog_entry_related_content')

        # Removing M2M table for field category on 'Entry'
        db.delete_table('blog_entry_category')

        # Removing M2M table for field blog on 'Entry'
        db.delete_table('blog_entry_blog')

        # Deleting model 'Distraction'
        db.delete_table('blog_distraction')

        # Deleting model 'FeedHit'
        db.delete_table('blog_feedhit')


    models = {
        'blog.blog': {
            'Meta': {'ordering': "['title']", 'object_name': 'Blog'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'blog.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'blog.distraction': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'Distraction'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'blog.entry': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'Entry'},
            'blog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Blog']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Category']", 'symmetrical': 'False'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'markup': ('django_markup.fields.MarkupField', [], {'default': "'textile'", 'max_length': '255'}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'read_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_content': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_content_rel_+'", 'null': 'True', 'to': "orm['blog.Entry']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'blog.feedhit': {
            'Meta': {'object_name': 'FeedHit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_data': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['blog']
