# Generated by Django 4.2 on 2023-05-14 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_created_date_alter_category_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_date']},
        ),
    ]