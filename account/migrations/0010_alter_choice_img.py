# Generated by Django 3.2.6 on 2021-12-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_choice_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='img',
            field=models.ImageField(default='/static/images/logo.svg', upload_to='media/'),
        ),
    ]
