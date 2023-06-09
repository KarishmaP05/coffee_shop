# Generated by Django 4.2 on 2023-05-08 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dozecafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('total_cost', models.IntegerField()),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cust_name', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='dozecafe.coffee')),
            ],
        ),
    ]
