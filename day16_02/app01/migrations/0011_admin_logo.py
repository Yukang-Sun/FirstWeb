# Generated by Django 4.2.2 on 2023-07-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_alter_logo_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='logo',
            field=models.ImageField(default='/media/default_logo.jpg', upload_to='user/'),
        ),
    ]
