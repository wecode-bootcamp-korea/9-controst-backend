# Generated by Django 3.0.7 on 2020-07-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounselCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('center_type', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('homepage_url', models.CharField(blank=True, max_length=2000, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('road_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_trost_partner', models.BooleanField(blank=True, default=False, null=True)),
                ('partner_info', models.CharField(blank=True, max_length=2000, null=True)),
                ('counseling_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'counselcenters',
            },
        ),
    ]
