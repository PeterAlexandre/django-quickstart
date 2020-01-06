# Generated by Django 3.0 on 2019-12-11 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191211_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('nationality', models.CharField(max_length=40)),
                ('naturalness', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.person',),
        ),
    ]
