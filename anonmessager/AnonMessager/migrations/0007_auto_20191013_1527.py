# Generated by Django 2.2.6 on 2019-10-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnonMessager', '0006_auto_20190925_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messages',
            field=models.TextField(max_length=250),
        ),
    ]
