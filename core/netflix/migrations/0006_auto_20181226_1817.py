# Generated by Django 2.1.4 on 2018-12-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netflix', '0005_auto_20181226_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='ator',
            name='nome',
            field=models.CharField(default='Olae', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ator',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'M'), (2, 'F')], default=1),
        ),
    ]
