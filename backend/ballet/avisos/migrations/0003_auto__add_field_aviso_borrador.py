# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Aviso.borrador'
        db.add_column(u'avisos_aviso', 'borrador',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Aviso.borrador'
        db.delete_column(u'avisos_aviso', 'borrador')


    models = {
        u'avisos.aviso': {
            'Meta': {'object_name': 'Aviso'},
            'borrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['avisos.Tag']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'avisos.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'avisos.urlaviso': {
            'Meta': {'object_name': 'UrlAviso'},
            'aviso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['avisos.Aviso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        }
    }

    complete_apps = ['avisos']