# Generated by Django 3.2.6 on 2021-08-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_alter_student_student_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_ovew',
            field=models.TextField(null=True),
        ),
    ]
