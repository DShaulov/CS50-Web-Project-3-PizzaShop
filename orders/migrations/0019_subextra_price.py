# Generated by Django 3.0.4 on 2020-03-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_remove_subextra_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subextra',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
