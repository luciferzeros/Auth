# Generated by Django 3.1.1 on 2020-09-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_snippet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]