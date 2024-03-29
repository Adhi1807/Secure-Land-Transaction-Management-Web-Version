# Generated by Django 3.2.8 on 2022-03-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_land_details_land_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land_details',
            old_name='hash_pass',
            new_name='hash_value',
        ),
        migrations.AddField(
            model_name='land_details',
            name='secret_password',
            field=models.CharField(default='none', max_length=300),
        ),
        migrations.AlterField(
            model_name='land_details',
            name='previous_buyer',
            field=models.CharField(max_length=250),
        ),
    ]
