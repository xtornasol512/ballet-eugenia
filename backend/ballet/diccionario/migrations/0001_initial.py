# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Palabra'
        db.create_table(u'diccionario_palabra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'diccionario', ['Palabra'])

        # Adding M2M table for field tags on 'Palabra'
        m2m_table_name = db.shorten_name(u'diccionario_palabra_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('palabra', models.ForeignKey(orm[u'diccionario.palabra'], null=False)),
            ('tag', models.ForeignKey(orm[u'diccionario.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['palabra_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'diccionario_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'diccionario', ['Tag'])

        # Adding model 'UrlPalabra'
        db.create_table(u'diccionario_urlpalabra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('palabra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diccionario.Palabra'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=225)),
        ))
        db.send_create_signal(u'diccionario', ['UrlPalabra'])


    def backwards(self, orm):
        # Deleting model 'Palabra'
        db.delete_table(u'diccionario_palabra')

        # Removing M2M table for field tags on 'Palabra'
        db.delete_table(db.shorten_name(u'diccionario_palabra_tags'))

        # Deleting model 'Tag'
        db.delete_table(u'diccionario_tag')

        # Deleting model 'UrlPalabra'
        db.delete_table(u'diccionario_urlpalabra')


    models = {
        u'diccionario.palabra': {
            'Meta': {'object_name': 'Palabra'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['diccionario.Tag']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'diccionario.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'diccionario.urlpalabra': {
            'Meta': {'object_name': 'UrlPalabra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palabra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diccionario.Palabra']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        }
    }

    complete_apps = ['diccionario']