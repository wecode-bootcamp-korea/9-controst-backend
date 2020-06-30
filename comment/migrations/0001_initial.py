# Generated by Django 3.0.7 on 2020-06-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.FloatField(default=2.5)),
                ('comment', models.CharField(max_length=10000)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.History')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Review')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Theme')),
            ],
            options={
                'db_table': 'reviews_themes',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='theme',
            field=models.ManyToManyField(related_name='review', through='comment.ReviewTheme', to='partner.Theme'),
        ),
    ]
