# Generated by Django 3.2.1 on 2021-05-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'On'), ('False', 'Off')], max_length=10),
        ),
    ]
