# Generated by Django 4.1.7 on 2023-03-01 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple_chat', '0003_rename_message_messagemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadmodel',
            name='participants',
            field=models.ManyToManyField(related_name='thread', to=settings.AUTH_USER_MODEL),
        ),
    ]
