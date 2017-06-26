from django.contrib.auth.models import User
from django.db import models


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='subcategory', blank=True, null=True)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


# Модель продукта
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, verbose_name="Категория",  blank=True, null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name']
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product)
    pass


class Customer(models.Model):
    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=200, db_index=True, verbose_name="Name")

    #def __unicode__(self):
    #    return self.user

    #password = models.
    #email = models.
    #first_name = models.
    #last_name = models.
    avatar = models.ImageField(upload_to='customer_avatar', blank=True, null=True, verbose_name="Avatar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    pass

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'