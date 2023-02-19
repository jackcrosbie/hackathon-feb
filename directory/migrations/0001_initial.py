# Generated by Django 3.2.18 on 2023-02-18 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('work', models.CharField(max_length=254)),
                ('summary', models.CharField(default='To be added', max_length=2000)),
                ('website', models.CharField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=254, null=True)),
                ('instagram', models.CharField(blank=True, max_length=254, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.location')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('summary', models.CharField(max_length=2000)),
                ('website', models.CharField(max_length=254)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.location')),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.org')),
            ],
        ),
    ]