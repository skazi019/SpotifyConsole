# Generated by Django 3.2.4 on 2021-06-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_analytics', '0002_auto_20210612_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotifytokens',
            name='profile_data',
            field=models.JSONField(default='{}'),
        ),
    ]
