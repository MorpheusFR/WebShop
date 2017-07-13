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
    user_name = models.CharField(max_length=200, default='', db_index=True, verbose_name="Name")

    #def __unicode__(self):
    #    return self.user


    # first_name = models.CharField(max_length=50, default=True, verbose_name='Имя')
    # last_name = models.CharField(max_length=50, default=True, verbose_name='Фамилия')
    # password = models.CharField(max_length=100, default=True)
    # phone = models.CharField(max_length=10, default=True, verbose_name='Телефон')
    # email = models.EmailField(default=True)
    # date_of_birth = models.DateField(default=True, verbose_name='Дата рождения')

    avatar = models.ImageField(upload_to='customer_avatar', blank=True, null=True, verbose_name="Avatar")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Обновлено")

    #orders =
    #reviews =
    #wishes =



    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Orders(models.Model):

    name = models.CharField(max_length=200, db_index=True, verbose_name="Заказы")
    quantity = models.PositiveIntegerField(verbose_name="Колличество")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    done = models.BooleanField(default=True, verbose_name="Выполнен")
    canceled = models.BooleanField(default=True, verbose_name="Отменен")
    orders = models.ForeignKey(Customer)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Reviews(models.Model):

    name = models.CharField(max_length=200, db_index=True, verbose_name="Отзывы")
    product = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    caption = models.CharField(max_length=200, db_index=True, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Текст отзыва")
    reviews = models.ForeignKey(Customer)

    stars = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'