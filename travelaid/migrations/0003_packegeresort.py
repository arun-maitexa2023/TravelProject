# Generated by Django 3.2.8 on 2023-07-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelaid', '0002_auto_20230714_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackegeResort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Packegename', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=50)),
                ('Startdate', models.CharField(max_length=50)),
                ('Enddate', models.CharField(max_length=50)),
                ('Bookingcount', models.CharField(max_length=50)),
                ('Packegestatus', models.CharField(max_length=50)),
                ('resortname', models.CharField(max_length=50)),
                ('Resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelaid.hotel')),
            ],
        ),
    ]