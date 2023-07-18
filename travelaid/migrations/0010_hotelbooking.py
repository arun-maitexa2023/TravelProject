# Generated by Django 3.2.8 on 2023-07-17 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0009_reels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotelbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotelname', models.CharField(max_length=50)),
                ('Checkindate', models.CharField(max_length=50)),
                ('Checkoutdate', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('Bookingstatus', models.CharField(max_length=50)),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.user')),
            ],
        ),
    ]