# Generated by Django 3.0.3 on 2022-01-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('Place', models.CharField(max_length=255)),
                ('postingDate', models.DateField(auto_now_add=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, default='#', null=True, upload_to='newsandevents')),
            ],
        ),
    ]