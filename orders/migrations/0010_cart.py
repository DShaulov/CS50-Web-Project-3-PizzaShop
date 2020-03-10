# Generated by Django 3.0.4 on 2020-03-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_dinnerplatter_pasta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('toppings', models.CharField(max_length=64)),
                ('extra', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
