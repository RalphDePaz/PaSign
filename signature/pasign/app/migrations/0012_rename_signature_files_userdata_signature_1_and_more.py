# Generated by Django 4.2.7 on 2023-11-24 03:57

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_userdata_signature_files_delete_signaturefile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='signature_files',
            new_name='signature_1',
        ),
        migrations.AddField(
            model_name='userdata',
            name='signature_2',
            field=models.FileField(blank=True, null=True, upload_to=app.models.get_user_signature_path),
        ),
        migrations.AddField(
            model_name='userdata',
            name='signature_3',
            field=models.FileField(blank=True, null=True, upload_to=app.models.get_user_signature_path),
        ),
    ]
