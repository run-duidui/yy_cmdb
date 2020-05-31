# Generated by Django 3.0.5 on 2020-05-24 16:29

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(blank=True, max_length=11, null=True)),
                ('sex', models.CharField(choices=[(1, '男'), (2, '女')], default=1, max_length=2)),
                ('picture', models.FileField(blank=True, null=True, upload_to=account.models.upload_to)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
