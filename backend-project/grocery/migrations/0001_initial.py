# Generated by Django 2.2 on 2020-06-14 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category Name', max_length=50)),
                ('image', models.ImageField(upload_to='categories')),
                ('ext_id', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('ext_id', models.CharField(blank=True, max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_summary_customer', to='users.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product Name', max_length=50)),
                ('image', models.ImageField(upload_to='products')),
                ('availability', models.CharField(choices=[('A', 'Available'), ('N', 'Not Available')], default='A', max_length=1)),
                ('price', models.DecimalField(decimal_places=5, help_text='Product Price for per unit', max_digits=15)),
                ('ext_id', models.CharField(blank=True, max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='grocery.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product Name', max_length=50)),
                ('status', models.CharField(choices=[('P', 'Pickup'), ('D', 'Delivery')], max_length=1)),
                ('transport_mode', models.CharField(choices=[('P', 'Pickup'), ('D', 'Delivery')], max_length=1)),
                ('total_price', models.DecimalField(decimal_places=5, help_text='Product Price for per unit', max_digits=15)),
                ('ext_id', models.CharField(blank=True, max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderSummary_customer', to='users.Customer')),
                ('ordered_item', models.ManyToManyField(blank=True, related_name='ordered_items', to='grocery.OrderedProduct')),
                ('vender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderSummary_customer', to='users.Vender')),
            ],
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_product_product', to='grocery.Product'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='vender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_summary_vender', to='users.Vender'),
        ),
    ]
