# Generated by Django 3.1.5 on 2021-01-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(max_length=10)),
                ('ename', models.CharField(max_length=20)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('elocn', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]