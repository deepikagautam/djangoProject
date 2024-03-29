# Generated by Django 2.2.2 on 2019-07-22 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address_details',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('house_no', models.CharField(max_length=200)),
                ('building_name', models.CharField(blank=True, max_length=200, null=True)),
                ('landmark', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='category_images/%Y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=20)),
                ('allowed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('contact_fname', models.CharField(max_length=50)),
                ('contact_lname', models.CharField(max_length=50)),
                ('contact_title', models.CharField(max_length=10)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('payment_method', models.CharField(max_length=15)),
                ('type_goods', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=255)),
                ('id_sku', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('quantity_per_unit', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_size', models.CharField(max_length=255)),
                ('available_colors', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_weight', models.CharField(max_length=255)),
                ('units_in_stock', models.PositiveIntegerField()),
                ('product_available', models.BooleanField(default=True)),
                ('discount_available', models.BooleanField(default=False)),
                ('picture1', models.ImageField(upload_to='product_images/%Y/%m/%d')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('picture5', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('picture6', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('picture7', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/%d')),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('note', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Category ID')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Supplier', verbose_name='Supplier ID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('payment_mode', models.CharField(max_length=10)),
                ('order_date', models.DateTimeField(verbose_name='order date')),
                ('ship_date', models.DateTimeField(verbose_name='ship date')),
                ('sales_tax', models.IntegerField()),
                ('transact_status', models.CharField(max_length=20)),
                ('fulfilled', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='payment date')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address_details', verbose_name='Address Id')),
                ('shipper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shipper', verbose_name='Shipper ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_sku', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('fulfilled', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('ship_date', models.DateTimeField(verbose_name='ship date')),
                ('bill_date', models.DateTimeField(verbose_name='bill date')),
                ('deliver_date', models.DateTimeField(verbose_name='deliver date')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Orders', verbose_name='Order ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product', verbose_name='Product ID')),
                ('shipping_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address_details', verbose_name='Address Id')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product', verbose_name='Product ID')),
            ],
        ),
    ]
