from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=60)
    image = models.TextField()
    image_file = models.ImageField(
        default="media/default_media/Portraits_2.png",
        upload_to="media/uploaded_media",
        null=True,
        blank=True,
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(
        "manga.Manga", on_delete=models.CASCADE, related_name="manga_comments"
    )
    text = models.TextField()
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} commented manga :{self.manga}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


# Create your models here.
