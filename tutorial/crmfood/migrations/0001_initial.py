# Generated by Django 2.2.3 on 2019-07-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meal_Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='deps', to='crmfood.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Persentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persentage', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('dateofadd', models.IntegerField(default=True)),
                ('roleid', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='crmfood.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('waiterid', models.IntegerField(default=True)),
                ('tableid', models.IntegerField(default=True)),
                ('tablename', models.CharField(max_length=50)),
                ('isitopen', models.IntegerField(default=True)),
                ('date', models.IntegerField(default=True)),
                ('mealsid', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='crmfood.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Meals_meal_by_category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=True)),
                ('decription', models.CharField(max_length=50)),
                ('categoryid', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals_meal_by_category', to='crmfood.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=True)),
                ('decription', models.CharField(max_length=50)),
                ('categoryid', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals', to='crmfood.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Meal_to_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.IntegerField(default=True)),
                ('orderid', models.IntegerField(default=True)),
                ('meals', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_to_order', to='crmfood.Meal_Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Meal_categories_for_Dep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='mcfd', to='crmfood.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('orderid', models.IntegerField(default=True)),
                ('date', models.IntegerField(default=True)),
                ('servicefee', models.IntegerField(default=True)),
                ('totalsum', models.IntegerField(default=True)),
                ('meals', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checks', to='crmfood.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Active_orders',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('waiterid', models.IntegerField(default=True)),
                ('isitopen', models.IntegerField(default=True)),
                ('date', models.IntegerField(default=True)),
                ('mealsid', models.IntegerField(default=True)),
                ('tablename', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='active_orders', to='crmfood.Roles')),
            ],
        ),
    ]