# Generated by Django 4.2.7 on 2023-12-01 22:38

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('planner', '0004_alter_trip_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='arrival',
            field=models.DateField(default=datetime.date(2023, 12, 4)),
        ),
    ]
