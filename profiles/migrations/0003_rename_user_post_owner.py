# Generated by Django 5.0.1 on 2024-02-19 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_user_options_alter_user_email_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
    ]
