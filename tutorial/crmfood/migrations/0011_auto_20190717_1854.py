# Generated by Django 2.2.3 on 2019-07-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmfood', '0010_auto_20190717_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dateofadd',
            field=models.CharField(max_length=20),
        ),
    ]
