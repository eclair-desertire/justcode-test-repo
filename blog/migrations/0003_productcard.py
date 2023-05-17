# Generated by Django 4.2 on 2023-05-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_role_alter_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
            ],
            options={
                'verbose_name': 'Карточка товара',
                'verbose_name_plural': 'Карточки товаров',
            },
        ),
    ]
