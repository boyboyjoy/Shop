# Generated by Django 3.2.3 on 2021-05-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='vendor_code',
            field=models.IntegerField(max_length=13),
        ),
        migrations.AlterField(
            model_name='salemodel',
            name='sale_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='supplymodel',
            name='supply_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='writeoffproductmodel',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
