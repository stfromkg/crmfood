# Generated by Django 2.2.3 on 2019-07-04 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmfood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal_categories_for_dep',
            old_name='department',
            new_name='departmentid',
        ),
        migrations.AlterField(
            model_name='active_orders',
            name='tablename',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='active_orders', to='crmfood.Tables'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='meals',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='crmfood.Meals'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='orderid',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='crmfood.Orders'),
        ),
        migrations.AlterField(
            model_name='meals',
            name='categoryid',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals', to='crmfood.Meals_meal_by_category'),
        ),
        migrations.AlterField(
            model_name='meals_meal_by_category',
            name='categoryid',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals_meal_by_category', to='crmfood.Meal_categories_for_Dep'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='mealsid',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='crmfood.Meal_to_Order'),
        ),
    ]
