from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, company, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, company=company)

        user.set_password(password)
        user.save()

        return user

class Company(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.EmailField(max_length=255,null=True)
    is_active = models.BooleanField(default=False)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE,null=True,blank=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','company','is_staff']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email