# Generated by Django 5.1 on 2024-10-04 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Record_maintain', '0018_employee_email_employee_empid_employee_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeefile',
            name='employee',
        ),
    ]
