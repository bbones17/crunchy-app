# Generated by Django 3.2.19 on 2024-06-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchy', '0004_auto_20240619_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='etiqueta',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
