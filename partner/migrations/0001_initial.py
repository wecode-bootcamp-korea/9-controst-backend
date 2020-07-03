from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('counsel_count', models.IntegerField(default=0)),
                ('introduction', models.CharField(max_length=1000)),
                ('is_counsel_count_gt_150', models.BooleanField(default=False)),
                ('profile_image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'counselors',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'duration',
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'kinds',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Duration')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Kind')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Level')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='CounselorTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Counselor')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Theme')),
            ],
            options={
                'db_table': 'counselor_themes',
            },
        ),
        migrations.CreateModel(
            name='CounselorKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Counselor')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Kind')),
            ],
            options={
                'db_table': 'counselor_kinds',
            },
        ),
        migrations.CreateModel(
            name='CounselorContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('counselor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partner.Counselor')),
            ],
            options={
                'db_table': 'counselor_contents',
            },
        ),
        migrations.AddField(
            model_name='counselor',
            name='kind',
            field=models.ManyToManyField(through='partner.CounselorKind', to='partner.Kind'),
        ),
        migrations.AddField(
            model_name='counselor',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Level'),
        ),
        migrations.AddField(
            model_name='counselor',
            name='theme',
            field=models.ManyToManyField(through='partner.CounselorTheme', to='partner.Theme'),
        ),
    ]
