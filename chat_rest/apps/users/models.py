from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, email, username, name, surname, password, is_admin):
        if not email:
            raise ValueError('user must has email!')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            admin_user=is_admin
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, name, surname, password=None):
        return self._create_user(email, username, name, surname, password, False)

    def create_superuser(self, email, username, name, surname, password):
        return self._create_user(email, username, name, surname, password, True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', unique=True, max_length=100)
    email = models.EmailField('email', unique=True, max_length=254)
    name = models.CharField('name', blank=True, null=True, max_length=200)
    surname = models.CharField(
        'surname',
        blank=True,
        null=True,
        max_length=200
    )
    avatar = models.ImageField(
        'user avatar image',
        upload_to='profile/',
        max_length=200,
        blank=True,
        null=True
    )
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin_user
