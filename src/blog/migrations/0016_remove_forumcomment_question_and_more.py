# Generated by Django 4.1.7 on 2023-05-15 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_forum_forumcomment_forumreply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumcomment',
            name='question',
        ),
        migrations.RemoveField(
            model_name='forumcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='forumreply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='forumreply',
            name='user',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.DeleteModel(
            name='ForumComment',
        ),
        migrations.DeleteModel(
            name='ForumReply',
        ),
    ]
