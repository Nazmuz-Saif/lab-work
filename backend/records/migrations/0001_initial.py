import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_code', models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]+$', 'Use only letters and digits.')])),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
            options={
                'db_table': 'Product',
                'ordering': ['product_code'],
            },
        ),
    ]
