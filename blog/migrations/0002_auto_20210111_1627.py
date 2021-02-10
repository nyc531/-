# Generated by Django 2.2.14 on 2021-01-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.CharField(max_length=500),
        ),
    ]