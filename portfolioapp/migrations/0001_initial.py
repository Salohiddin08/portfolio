# Generated by Django 5.1.4 on 2024-12-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Project Title')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='Project Image')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Project URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
