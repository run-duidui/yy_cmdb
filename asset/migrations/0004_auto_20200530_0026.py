# Generated by Django 3.0.5 on 2020-05-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20200530_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='host_group',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
