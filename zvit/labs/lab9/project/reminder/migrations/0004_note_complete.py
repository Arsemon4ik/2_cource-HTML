# Generated by Django 4.0 on 2021-12-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_rename_notes_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
