from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_human(self, username, nickname, image_file, password, **extra):
        user = self.model(
            username=username, nickname=nickname, image_file=image_file, **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_human(self, username, nickname, image_file, password):
        return self._create_human(
            username,
            nickname,
            image_file,
            password,
        )

    def _create_user(self, username, nickname, image, password, **extra):
        user = self.model(username=username, nickname=nickname, image=image, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_admin(self, username, password, **extra):
        admin = self.model(username=username, password=password, **extra)
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_user(self, username, nickname, image, password):
        return self._create_user(username, nickname, image, password)

    def create_superuser(self, username, password):
        return self._create_admin(
            username, password, is_superuser=True, is_staff=True
        )
