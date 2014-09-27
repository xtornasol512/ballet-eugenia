# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Perfil'
        db.create_table(u'perfiles_perfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('biografia', self.gf('django.db.models.fields.TextField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('domicilio', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('genero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.Genero'])),
        ))
        db.send_create_signal(u'perfiles', ['Perfil'])

        # Adding model 'Genero'
        db.create_table(u'perfiles_genero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'perfiles', ['Genero'])

        # Adding model 'Telefono'
        db.create_table(u'perfiles_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.TipoTelefono'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('perfil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.Perfil'])),
        ))
        db.send_create_signal(u'perfiles', ['Telefono'])

        # Adding model 'TipoTelefono'
        db.create_table(u'perfiles_tipotelefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'perfiles', ['TipoTelefono'])

        # Adding model 'UrlPerfil'
        db.create_table(u'perfiles_urlperfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('perfil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.Perfil'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=225)),
        ))
        db.send_create_signal(u'perfiles', ['UrlPerfil'])


    def backwards(self, orm):
        # Deleting model 'Perfil'
        db.delete_table(u'perfiles_perfil')

        # Deleting model 'Genero'
        db.delete_table(u'perfiles_genero')

        # Deleting model 'Telefono'
        db.delete_table(u'perfiles_telefono')

        # Deleting model 'TipoTelefono'
        db.delete_table(u'perfiles_tipotelefono')

        # Deleting model 'UrlPerfil'
        db.delete_table(u'perfiles_urlperfil')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'perfiles.genero': {
            'Meta': {'object_name': 'Genero'},
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfiles.perfil': {
            'Meta': {'object_name': 'Perfil'},
            'biografia': ('django.db.models.fields.TextField', [], {}),
            'domicilio': ('django.db.models.fields.TextField', [], {}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfiles.Genero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'perfiles.telefono': {
            'Meta': {'object_name': 'Telefono'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfiles.Perfil']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfiles.TipoTelefono']"})
        },
        u'perfiles.tipotelefono': {
            'Meta': {'object_name': 'TipoTelefono'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'perfiles.urlperfil': {
            'Meta': {'object_name': 'UrlPerfil'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfiles.Perfil']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        }
    }

    complete_apps = ['perfiles']