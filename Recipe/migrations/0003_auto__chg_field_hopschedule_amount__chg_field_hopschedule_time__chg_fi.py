# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HopSchedule.amount'
        db.alter_column('Recipe_hopschedule', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

        # Changing field 'HopSchedule.time'
        db.alter_column('Recipe_hopschedule', 'time', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Hop.use'
        db.alter_column('Recipe_hop', 'use', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Hop.alpha_acid'
        db.alter_column('Recipe_hop', 'alpha_acid', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1))

        # Changing field 'MiscBill.use'
        db.alter_column('Recipe_miscbill', 'use', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Yeast.attenuation'
        db.alter_column('Recipe_yeast', 'attenuation', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Yeast.flocculation'
        db.alter_column('Recipe_yeast', 'flocculation', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):

        # Changing field 'HopSchedule.amount'
        db.alter_column('Recipe_hopschedule', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

        # Changing field 'HopSchedule.time'
        db.alter_column('Recipe_hopschedule', 'time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Hop.use'
        db.alter_column('Recipe_hop', 'use', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Hop.alpha_acid'
        db.alter_column('Recipe_hop', 'alpha_acid', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3))

        # Changing field 'MiscBill.use'
        db.alter_column('Recipe_miscbill', 'use', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Yeast.attenuation'
        db.alter_column('Recipe_yeast', 'attenuation', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3))

        # Changing field 'Yeast.flocculation'
        db.alter_column('Recipe_yeast', 'flocculation', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3))

    models = {
        'Recipe.comments': {
            'Meta': {'object_name': 'Comments'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Recipe']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'Recipe.fermentable': {
            'Meta': {'object_name': 'Fermentable'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'potential_extract': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'use': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'Recipe.grainbill': {
            'Meta': {'object_name': 'GrainBill'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'fermentable_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Fermentable']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Recipe']"}),
            'use': ('django.db.models.fields.IntegerField', [], {})
        },
        'Recipe.hop': {
            'Meta': {'object_name': 'Hop'},
            'alpha_acid': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'use': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'Recipe.hopschedule': {
            'Meta': {'object_name': 'HopSchedule'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'hop_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Hop']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Recipe']"}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'use': ('django.db.models.fields.IntegerField', [], {})
        },
        'Recipe.misc': {
            'Meta': {'object_name': 'Misc'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'Recipe.miscbill': {
            'Meta': {'object_name': 'MiscBill'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'misc_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Misc']"}),
            'recipe_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Recipe']"}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'use': ('django.db.models.fields.IntegerField', [], {})
        },
        'Recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Recipe']", 'null': 'True', 'blank': 'True'}),
            'style_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Recipe.Style']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'yeast_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'Recipe.style': {
            'Meta': {'object_name': 'Style'},
            'color': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'final_gravity': ('django.db.models.fields.IntegerField', [], {}),
            'ibu_max': ('django.db.models.fields.IntegerField', [], {}),
            'ibu_min': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'original_gravity': ('django.db.models.fields.IntegerField', [], {})
        },
        'Recipe.yeast': {
            'Meta': {'object_name': 'Yeast'},
            'attenuation': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'flocculation': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Recipe']