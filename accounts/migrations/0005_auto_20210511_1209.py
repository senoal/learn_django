# Generated by Django 3.2.2 on 2021-05-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210511_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
