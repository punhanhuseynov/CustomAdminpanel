# Generated by Django 4.2 on 2023-04-26 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0003_users_is_active_users_is_staff_users_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='is_staff',
            new_name='is_admin',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
    ]
