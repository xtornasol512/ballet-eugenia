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
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Alumno'])),
            ('biografia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('domicilio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('genero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.Genero'], null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('editable', self.gf('django.db.models.fields.BooleanField')(default=True)),
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
        u'perfiles.genero': {
            'Meta': {'object_name': 'Genero'},
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfiles.perfil': {
            'Meta': {'object_name': 'Perfil'},
            'biografia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'domicilio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfiles.Genero']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Alumno']"})
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
        },
        u'usuarios.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'usuarios.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literal': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            'profesor': ('django.db.models.fields.CharField', [], {'default': "'Miss Gennita'", 'max_length': '255'})
        }
    }

    complete_apps = ['perfiles']