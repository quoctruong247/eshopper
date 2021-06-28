# Generated by Django 3.2.4 on 2021-06-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210609_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settinglang',
            old_name='contact',
            new_name='contactus',
        ),
        migrations.AlterField(
            model_name='faq',
            name='lang',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('vi', 'Vietnamese')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='settinglang',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('vi', 'Vietnamese')], max_length=6),
        ),
    ]
