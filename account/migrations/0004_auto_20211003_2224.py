# Generated by Django 3.2.6 on 2021-10-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210915_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dept',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Information Systems', 'Information Systems'), ('Software Engineering', 'Software Engineering'), ('Information Technology', 'Information Technology'), ('Cybersecurity', 'Cybersecurity')], default='Computer Science', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')], default='100', max_length=100),
        ),
    ]