# Generated by Django 2.1 on 2018-08-22 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionaloffer',
            name='condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='offer.Condition'),
        ),
    ]
