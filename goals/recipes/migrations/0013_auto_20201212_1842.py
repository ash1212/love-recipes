# Generated by Django 3.0.6 on 2020-12-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20201212_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.DurationField(),
        ),
    ]