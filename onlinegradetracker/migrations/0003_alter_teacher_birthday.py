# Generated by Django 4.2.6 on 2023-12-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinegradetracker', '0002_alter_student_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Birthday',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]