# Generated by Django 3.1.5 on 2021-01-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210124_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.TextField(),
        ),
    ]
