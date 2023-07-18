# Generated by Django 3.2.8 on 2023-07-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0012_auto_20230717_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='Hotels',
            new_name='Hotel',
        ),
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='users',
            new_name='user',
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='Hotelname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='Bookingstatus',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='Checkindate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='Checkintime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='Checkoutdate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='noofpersons',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]