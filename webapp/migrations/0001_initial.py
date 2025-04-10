# Generated by Django 3.1 on 2025-04-10 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.TextField(verbose_name='main sentence...')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
            ],
        ),
    ]
