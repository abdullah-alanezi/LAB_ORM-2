# Generated by Django 4.2.7 on 2023-11-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_op', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='published',
            name='published_at',
            field=models.BooleanField(default=True),
        ),
    ]
