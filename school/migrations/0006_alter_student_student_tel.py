# Generated by Django 3.2.5 on 2021-08-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_student_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_tel',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
