# Generated by Django 3.1.5 on 2021-01-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210111_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.CharField(max_length=2000),
        ),
    ]