# Generated by Django 4.0.3 on 2022-05-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0007_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image9',
        ),
        migrations.RemoveField(
            model_name='project',
            name='on_if_left',
        ),
        migrations.AlterField(
            model_name='project',
            name='image_cover',
            field=models.ImageField(upload_to='my_projects/images/'),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
