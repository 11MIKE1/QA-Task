# Generated by Django 4.2.3 on 2023-10-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_linkoptionblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eighth_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_1', models.CharField(blank=True, max_length=100, verbose_name='Ссылки навигации №1')),
                ('url_2', models.CharField(blank=True, max_length=100, verbose_name='Ссылки навигации №2')),
                ('url_3', models.CharField(blank=True, max_length=100, verbose_name='Ссылки навигации №3')),
            ],
            options={
                'verbose_name': 'Восьмой раздел-Ссылки навигации',
                'verbose_name_plural': 'Восьмой раздел-Ссылки навигации',
            },
        ),
        migrations.DeleteModel(
            name='LinkOptionBlock',
        ),
    ]
