# Generated by Django 4.1.1 on 2022-09-21 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='uzsakymas_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uzsakymoeilute', to='autoservice.uzsakymas'),
        ),
    ]
