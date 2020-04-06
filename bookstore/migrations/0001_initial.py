# Generated by Django 3.0.5 on 2020-04-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=50, verbose_name='书名')),
                ('pub_house', models.CharField(default='', max_length=100, verbose_name='出版社')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='定价')),
                ('market_price', models.DecimalField(decimal_places=2, default=9999, max_digits=7, verbose_name='零售价')),
            ],
        ),
    ]
