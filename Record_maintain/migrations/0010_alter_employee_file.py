# Generated by Django 5.1 on 2024-08-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_maintain', '0009_alter_employee_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
