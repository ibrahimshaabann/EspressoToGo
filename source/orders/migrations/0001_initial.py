# Generated by Django 4.2.5 on 2023-09-27 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('CANCELED', 'Canceled'), ('DONE', 'Done')], default='PENDING', max_length=12)),
                ('order_type', models.CharField(choices=[('HALL', 'Hall'), ('DELIVERY', 'Delivery'), ('TAKEAWAY', 'TakeAway')], default='HALL', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'db_table': 'order_items',
                'ordering': ['-id'],
            },
        ),
    ]
