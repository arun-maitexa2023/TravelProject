# Generated by Django 3.2.8 on 2023-07-17 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0014_rename_hotel_hotelbooking_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resortbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resortname', models.CharField(max_length=50)),
                ('noofpersons', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('Checkindate', models.CharField(max_length=50)),
                ('Checkintime', models.CharField(max_length=50)),
                ('Checkoutdate', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('Bookingstatus', models.CharField(max_length=50)),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.resort')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
    ]
