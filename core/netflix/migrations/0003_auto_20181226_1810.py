# Generated by Django 2.1.4 on 2018-12-26 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netflix', '0002_auto_20181226_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='produtora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='netflix.Produtora'),
        ),
    ]
