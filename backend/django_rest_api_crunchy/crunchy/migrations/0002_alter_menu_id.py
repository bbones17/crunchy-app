# Generated by Django 3.2.19 on 2024-06-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
