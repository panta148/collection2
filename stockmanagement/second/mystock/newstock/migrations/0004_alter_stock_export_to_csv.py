# Generated by Django 3.2.9 on 2021-11-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstock', '0003_alter_stock_export_to_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='export_to_CSV',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
