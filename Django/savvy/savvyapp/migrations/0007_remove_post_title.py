# Generated by Django 5.0.6 on 2024-06-30 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savvyapp', '0006_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
