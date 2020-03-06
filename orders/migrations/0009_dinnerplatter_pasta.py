# Generated by Django 3.0.4 on 2020-03-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
