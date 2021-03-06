# Generated by Django 3.2.6 on 2021-08-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem',
            name='Mem_img',
            field=models.ImageField(default='', null=True, upload_to='member/%Y-%m-%d', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='Mem_id',
            field=models.CharField(max_length=200, unique=True, verbose_name='회원아이디'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='Mem_name',
            field=models.CharField(max_length=200, verbose_name='회원 이름'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='Mem_pwd',
            field=models.CharField(max_length=200, verbose_name='회원비밀번호'),
        ),
    ]
