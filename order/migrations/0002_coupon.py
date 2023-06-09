# Generated by Django 3.2 on 2023-04-06 00:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, verbose_name='code')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='value')),
                ('from_date', models.DateField(default=django.utils.timezone.now, verbose_name='from_date')),
                ('to_date', models.DateField(default=django.utils.timezone.now, verbose_name='from_date')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('image', models.ImageField(blank=True, null=True, upload_to='coupon/')),
            ],
        ),
    ]
