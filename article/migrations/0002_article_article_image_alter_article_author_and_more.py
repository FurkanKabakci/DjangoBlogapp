# Generated by Django 5.0.1 on 2024-01-24 22:50

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Icerik'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Olusturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Baslik'),
        ),
    ]
