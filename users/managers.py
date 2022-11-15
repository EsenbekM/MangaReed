from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, nickname, image, password, **extra):
        user = self.model(username=username, nickname=nickname, image=image, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, nickname, image, password):
        return self._create_user(username, nickname, image, password)

    def create_superuser(self, username, nickname, password):
        return self._create_user(
            username, nickname, password, is_superuser=True, is_staff=True
        )


