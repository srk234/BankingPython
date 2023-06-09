# Generated by Django 4.1.4 on 2023-05-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_delete_account_person_account_person_materials_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.CharField(choices=[('', 'Select an account type'), ('Current', 'Current'), ('Savings', 'Savings')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='materials',
            field=models.BooleanField(null=True),
        ),
    ]
