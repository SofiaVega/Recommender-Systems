# Generated by Django 4.0 on 2022-01-14 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Recommender_System_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='UserInfo',
        ),
    ]