# Generated by Django 4.1.4 on 2023-05-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_person_materials'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='materials',
            new_name='ChequeBook',
        ),
        migrations.AddField(
            model_name='person',
            name='Creditcard',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='Debitcard',
            field=models.BooleanField(default=True),
        ),
    ]
