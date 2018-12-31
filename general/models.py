from django.db import models


class Contacts(models.Model):
    phone = models.CharField(
        max_length=32,
        verbose_name='Номер телефону',
    )
    instagram = models.CharField(
        max_length=32,
        verbose_name='Instagram',
        blank=True
    )
    facebook = models.CharField(
        max_length=32,
        verbose_name='Facebook',
        blank=True
    )
    skype = models.CharField(
        max_length=32,
        verbose_name='Skype',
        blank=True
    )
    email = models.EmailField(
        verbose_name='Номер телефону',
        blank=True
    )
    address = models.CharField(
        max_length=128,
        verbose_name='Адреса',
        blank=True
    )

    class Meta:
        verbose_name = 'Контакти'
        verbose_name_plural = 'Контакти'

    def __str__(self):
        return self.phone


class Tastes(models.Model):
    taste_type = models.CharField(
        max_length=32,
    )
    available = models.BooleanField(
        default=True,
        verbose_name='Доступність'
    )

    class Meta:
        verbose_name = 'Смак'
        verbose_name_plural = 'Смаки'

    def __str__(self):
        return self.taste_type



