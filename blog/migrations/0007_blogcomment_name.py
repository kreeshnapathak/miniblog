# Generated by Django 3.2.3 on 2021-06-22 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210622_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='name',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
