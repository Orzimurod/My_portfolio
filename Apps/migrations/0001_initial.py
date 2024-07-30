# Generated by Django 5.0.7 on 2024-07-25 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon raqami quyidagi formatda kiritilishi kerak: '+9989########'. 12 tagacha raqamga ruxsat beriladi.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/portfolio')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/posts')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]