# Generated by Django 4.2 on 2023-05-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_sell_post_category_sell_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
