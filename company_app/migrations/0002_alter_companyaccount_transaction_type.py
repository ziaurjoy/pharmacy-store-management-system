# Generated by Django 4.2.1 on 2023-05-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyaccount',
            name='transaction_type',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=25),
        ),
    ]
