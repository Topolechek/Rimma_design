# Generated by Django 4.0.3 on 2022-05-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
    ]