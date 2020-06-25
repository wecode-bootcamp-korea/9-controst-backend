# Generated by Django 3.0.7 on 2020-06-25 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounselKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsel_kind', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'counsel_kinds',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'durations',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=19)),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('counsel_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.CounselKind')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Duration')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Level')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('counsel_count', models.IntegerField(default=0)),
                ('introduction', models.CharField(max_length=1000)),
                ('is_counsel_gt_150', models.IntegerField(default=0)),
                ('profile_image_url', models.URLField()),
                ('counsel_kinds', models.ManyToManyField(to='partner.CounselKind')),
                ('counsel_themes', models.ManyToManyField(to='partner.Theme')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Level')),
            ],
            options={
                'db_table': 'counselors',
            },
        ),
    ]
