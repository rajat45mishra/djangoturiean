# Generated by Django 2.2.1 on 2019-05-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addasset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assettype', models.CharField(max_length=50)),
                ('Assetsequence', models.CharField(max_length=50)),
                ('Assetname', models.CharField(max_length=50)),
                ('Assetnumber', models.CharField(max_length=50)),
                ('DateofPurchase', models.DateField()),
                ('AssestWarrentyUpto', models.DateField()),
            ],
        ),
    ]
