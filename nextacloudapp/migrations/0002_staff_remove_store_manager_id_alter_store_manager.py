# Generated by Django 4.0.2 on 2023-08-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nextacloudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(blank=True, max_length=200, null=True)),
                ('staff_position', models.CharField(blank=True, max_length=200, null=True)),
                ('staff_smartcard_number', models.IntegerField(blank=True, null=True)),
                ('staff_smartcard_color', models.CharField(blank=True, max_length=200, null=True)),
                ('staff_date_of_birth', models.DateField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('home_address', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone_number', models.IntegerField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=200, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='manager_id',
        ),
        migrations.AlterField(
            model_name='store',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nextacloudapp.staff'),
        ),
    ]
