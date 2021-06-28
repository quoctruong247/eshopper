# Generated by Django 3.2.1 on 2021-06-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_color_size_variants'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10),
        ),
    ]