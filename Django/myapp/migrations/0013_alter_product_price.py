# Generated by Django 5.1.3 on 2024-11-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_customer_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
