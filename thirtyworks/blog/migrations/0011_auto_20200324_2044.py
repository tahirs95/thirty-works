# Generated by Django 2.2 on 2020-03-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_anything_else'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='number',
            field=models.IntegerField(verbose_name='Day Number'),
        ),
    ]