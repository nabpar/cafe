# Generated by Django 5.0.6 on 2024-07-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_remove_bill_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bill",
            name="order_item",
        ),
        migrations.AddField(
            model_name="bill",
            name="order_items",
            field=models.ManyToManyField(to="product.order"),
        ),
    ]
