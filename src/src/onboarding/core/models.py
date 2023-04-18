from django.db import models


class OfficeMap(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    photo = models.ImageField(upload_to="images/", verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "План офиса"
        verbose_name_plural = "Планы офиса"
        ordering = ["id", "title"]


class Users(models.Model):
    user_id = models.PositiveBigIntegerField(primary_key=True, verbose_name="ID")
    username = models.CharField(max_length=32, null=True, blank=True, verbose_name="Полное имя")
    first_name = models.CharField(max_length=256, verbose_name="Имя", null=True, blank=True)
    last_name = models.CharField(max_length=256, verbose_name="Фамилия", null=True, blank=True)
    language_code = models.CharField(max_length=8, help_text="Язык пользователя в телеграмме", null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'



