# Generated by Django 5.1.2 on 2024-12-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default,jpeg', upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('admin_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]