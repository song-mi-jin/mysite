# Generated by Django 3.2.5 on 2021-08-04 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_subject_subject_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
