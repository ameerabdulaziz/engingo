# Generated by Django 3.2 on 2023-01-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='param_search_name',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]