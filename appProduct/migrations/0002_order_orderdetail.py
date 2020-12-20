# Generated by Django 2.2.5 on 2020-12-20 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appProduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='XXXXXXX', max_length=256)),
                ('state', models.CharField(default='Waiting', max_length=256)),
                ('totalprice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('totalprice', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProduct.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProduct.Product')),
            ],
        ),
    ]
