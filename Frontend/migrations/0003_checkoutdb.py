# Generated by Django 4.2.6 on 2023-12-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, max_length=100, null=True)),
                ('EmailId', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Telephone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
