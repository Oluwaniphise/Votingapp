# Generated by Django 3.2.6 on 2021-12-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='img',
            field=models.ImageField(default='images/candidate.jpg', upload_to='images/'),
        ),
    ]
