# Generated by Django 3.1 on 2020-08-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=20)),
                ('courseID', models.CharField(max_length=20)),
                ('courseName', models.CharField(max_length=20)),
            ],
        ),
    ]