# Generated by Django 4.2.5 on 2023-11-01 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('CANCELED', 'Canceled'), ('DONE', 'Done')], default='PENDING', max_length=12, verbose_name='حالة الاوردر')),
                ('order_type', models.CharField(choices=[('HALL', 'Hall'), ('DELIVERY', 'Delivery'), ('TAKEAWAY', 'TakeAway')], default='HALL', max_length=12, verbose_name='نوع الاوردر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='وقت الاودر')),
                ('total_price_of_order', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='اجمالي السعر')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address', verbose_name='العنوان ')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'الاوردرات',
                'db_table': 'orders',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='الكمية')),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='سعر العنصر')),
                ('total_price_of_order_items', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='اجمالي العناصر')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='products.menu', verbose_name='الاسم')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order', verbose_name='الاوردر')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'عناصر الاوردر',
                'db_table': 'order_items',
                'ordering': ['-id'],
            },
        ),
    ]
