# Generated by Django 4.2.7 on 2023-12-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashFlow', '0005_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]