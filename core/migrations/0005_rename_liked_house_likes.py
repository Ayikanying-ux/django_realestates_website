# Generated by Django 4.0 on 2022-01-06 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_likes_house_liked_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='liked',
            new_name='likes',
        ),
    ]