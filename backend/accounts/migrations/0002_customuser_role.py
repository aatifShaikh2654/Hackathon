# Generated by Django 5.0.7 on 2024-07-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('librarian', 'librarian'), ('user', 'user')], default='user', max_length=100),
        ),
    ]
