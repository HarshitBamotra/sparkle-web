# Generated by Django 3.2.3 on 2022-01-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
