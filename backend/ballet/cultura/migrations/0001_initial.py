# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'cultura_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'cultura', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name(u'cultura_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'cultura.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])

        # Adding model 'UrlPost'
        db.create_table(u'cultura_urlpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cultura.Post'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=225)),
        ))
        db.send_create_signal(u'cultura', ['UrlPost'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'cultura_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name(u'cultura_post_tags'))

        # Deleting model 'UrlPost'
        db.delete_table(u'cultura_urlpost')


    models = {
        u'cultura.post': {
            'Meta': {'object_name': 'Post'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'cultura.urlpost': {
            'Meta': {'object_name': 'UrlPost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cultura.Post']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cultura']