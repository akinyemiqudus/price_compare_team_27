# Generated by Django 4.0.6 on 2022-07-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare_app', '0002_remove_phone_price_komga_phone_price_konga_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='review_stars',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
    ]