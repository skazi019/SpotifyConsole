# Generated by Django 3.2.4 on 2021-06-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_analytics', '0003_spotifytokens_profile_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytokens',
            name='profile_data',
            field=models.JSONField(default={}),
        ),
    ]
