# Generated by Django 4.2.8 on 2023-12-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Description', models.TextField()),
                ('Year', models.IntegerField()),
                ('Images', models.ImageField(upload_to='img')),
            ],
        ),
    ]