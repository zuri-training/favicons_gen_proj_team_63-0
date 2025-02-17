# Generated by Django 4.0.6 on 2022-08-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favigen', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favicons',
            new_name='Favicon',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
