# Generated by Django 3.2.9 on 2021-11-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diveapi', '0002_sharkfact_shark_fact_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharkfact',
            name='shark_fact_title',
            field=models.CharField(max_length=500),
        ),
    ]