# Generated by Django 4.2 on 2023-05-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField()),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]