# Generated by Django 5.0.6 on 2024-07-07 18:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_bill"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bill",
            name="updated_at",
        ),
    ]
