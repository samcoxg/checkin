# Generated by Django 3.2.5 on 2021-12-31 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milkfeeding',
            name='ate_at',
        ),
    ]
