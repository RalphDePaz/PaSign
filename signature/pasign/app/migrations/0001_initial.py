# Generated by Django 4.2.7 on 2023-11-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('signature_type', models.CharField(max_length=50)),
            ],
        ),
    ]
