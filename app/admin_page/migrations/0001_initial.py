# Generated by Django 4.2 on 2023-04-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]