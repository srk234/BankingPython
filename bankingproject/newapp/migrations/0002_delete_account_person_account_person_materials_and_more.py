# Generated by Django 4.1.4 on 2023-05-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='person',
            name='account',
            field=models.CharField(choices=[('', 'Select an account type'), ('savings', 'savings'), ('current', 'current')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='materials',
            field=models.CharField(choices=[('1', 'credit card'), ('2', 'debit card'), ('3', 'cheque book')], default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]
