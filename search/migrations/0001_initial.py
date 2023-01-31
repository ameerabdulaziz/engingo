# Generated by Django 3.2 on 2023-01-31 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('url', models.URLField(max_length=120)),
                ('card_class', models.CharField(max_length=250)),
                ('title_class', models.CharField(max_length=250)),
                ('anchor_class', models.CharField(max_length=250)),
                ('description_class', models.CharField(max_length=250)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestSiteLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('response', models.TextField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.site')),
            ],
        ),
    ]
