# Generated by Django 4.2.1 on 2023-05-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='total_budget',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='total_expense',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='total_expense',
            field=models.FloatField(null=True),
        ),
    ]
