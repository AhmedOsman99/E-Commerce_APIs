# Generated by Django 4.2.2 on 2023-06-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='products.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='users.usermodel')),
            ],
        ),
    ]
