# Generated by Django 5.1 on 2024-08-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_maintain', '0005_alter_employee_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
