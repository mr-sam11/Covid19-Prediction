# Generated by Django 4.0.5 on 2022-06-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='landmark',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
