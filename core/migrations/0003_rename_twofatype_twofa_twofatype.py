# Generated by Django 3.2.9 on 2021-11-14 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_message_signin_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twofa',
            old_name='twoFAType',
            new_name='twoFaType',
        ),
    ]
