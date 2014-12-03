# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'diccionario_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'diccionario', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'diccionario_tag')


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