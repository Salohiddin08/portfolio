# Generated by Django 5.1.4 on 2024-12-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_contact_delete_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]