# Generated by Django 2.2.4 on 2019-09-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnonMessager', '0004_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=11111111, max_length=50),
            preserve_default=False,
        ),
    ]
