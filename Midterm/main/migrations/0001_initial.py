# Generated by Django 3.1 on 2021-03-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Book Journal Name')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200, verbose_name='Book Journal Description')),
                ('created_at', models.DateTimeField(verbose_name='Journal Date')),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Book Journal Name')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200, verbose_name='Book Journal Description')),
                ('created_at', models.DateTimeField(verbose_name='Journal Date')),
                ('type', models.IntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')], default=1, verbose_name='Type of Journal')),
                ('publisher', models.CharField(max_length=100, verbose_name='Publisher')),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
            },
        ),
    ]
