# Generated by Django 3.1 on 2021-05-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TraficEchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_trafic', models.URLField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'trafic_echange',
                'managed': False,
            },
        ),
    ]
