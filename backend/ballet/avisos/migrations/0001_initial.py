# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aviso'
        db.create_table(u'avisos_aviso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'avisos', ['Aviso'])

        # Adding M2M table for field tags on 'Aviso'
        m2m_table_name = db.shorten_name(u'avisos_aviso_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aviso', models.ForeignKey(orm[u'avisos.aviso'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['aviso_id', 'tag_id'])

        # Adding model 'UrlAviso'
        db.create_table(u'avisos_urlaviso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aviso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['avisos.Aviso'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=225)),
        ))
        db.send_create_signal(u'avisos', ['UrlAviso'])


    def backwards(self, orm):
        # Deleting model 'Aviso'
        db.delete_table(u'avisos_aviso')

        # Removing M2M table for field tags on 'Aviso'
        db.delete_table(db.shorten_name(u'avisos_aviso_tags'))

        # Deleting model 'UrlAviso'
        db.delete_table(u'avisos_urlaviso')


    models = {
        u'avisos.aviso': {
            'Meta': {'object_name': 'Aviso'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'avisos.urlaviso': {
            'Meta': {'object_name': 'UrlAviso'},
            'aviso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['avisos.Aviso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['avisos']