# Generated by Django 4.0.4 on 2022-05-22 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_created',
            new_name='due_date',
        ),
    ]
