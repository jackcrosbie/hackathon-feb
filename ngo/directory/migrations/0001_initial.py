# Generated by Django 3.2.18 on 2023-02-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrgDirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('work', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=254)),
                ('summary', models.CharField(default='To be added', max_length=2000)),
                ('website', models.CharField(blank=True, max_length=254, null=True)),
                ('facebook', models.CharField(max_length=254)),
                ('instagram', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=254)),
                ('summary', models.CharField(max_length=2000)),
                ('website', models.CharField(blank=True, max_length=254, null=True)),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.orgdirectory')),
            ],
        ),
    ]