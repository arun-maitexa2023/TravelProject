# Generated by Django 3.2.8 on 2023-07-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0007_auto_20230715_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatcommunity',
            name='Chat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatcommunity',
            name='Createdtime',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatcommunity',
            name='Uploaddate',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
