# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Perfil.nombre'
        db.delete_column(u'perfiles_perfil', 'nombre')

        # Adding field 'Perfil.twitter'
        db.add_column(u'perfiles_perfil', 'twitter',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Perfil.facebook'
        db.add_column(u'perfiles_perfil', 'facebook',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Perfil.editable'
        db.add_column(u'perfiles_perfil', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Perfil.edad'
        db.alter_column(u'perfiles_perfil', 'edad', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Perfil.biografia'
        db.alter_column(u'perfiles_perfil', 'biografia', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Perfil.genero'
        db.alter_column(u'perfiles_perfil', 'genero_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.Genero'], null=True))

        # Changing field 'Perfil.imagen'
        db.alter_column(u'perfiles_perfil', 'imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Perfil.usuario'
        db.alter_column(u'perfiles_perfil', 'usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Alumno']))

        # Changing field 'Perfil.domicilio'
        db.alter_column(u'perfiles_perfil', 'domicilio', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Adding field 'Perfil.nombre'
        db.add_column(u'perfiles_perfil', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='nada', max_length=255),
                      keep_default=False)

        # Deleting field 'Perfil.twitter'
        db.delete_column(u'perfiles_perfil', 'twitter')

        # Deleting field 'Perfil.facebook'
        db.delete_column(u'perfiles_perfil', 'facebook')

        # Deleting field 'Perfil.editable'
        db.delete_column(u'perfiles_perfil', 'editable')


        # Changing field 'Perfil.edad'
        db.alter_column(u'perfiles_perfil', 'edad', self.gf('django.db.models.fields.CharField')(default=0, max_length=2))

        # Changing field 'Perfil.biografia'
        db.alter_column(u'perfiles_perfil', 'biografia', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Perfil.genero'
        db.alter_column(u'perfiles_perfil', 'genero_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['perfiles.Genero']))

        # Changing field 'Perfil.imagen'
        db.alter_column(u'perfiles_perfil', 'imagen', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Perfil.usuario'
        db.alter_column(u'perfiles_perfil', 'usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Perfil.domicilio'
        db.alter_column(u'perfiles_perfil', 'domicilio', self.gf('django.db.models.fields.TextField')(default=''))

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