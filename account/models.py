import arrow
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
from django.db import models

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, null=False,default='NULL',unique=True)
    first_name = models.CharField(max_length=150, null=False,default='NULL')
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    introduction = models.TextField()
    # is_staff = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def get_shortname(self):
        return self.username

    def get_full_name(self):

        full_name = None

        if self.first_name or self.last_name:
            full_name = self.first_name+" "+self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    @property
    def created_on_arrow(self):
        return arrow.get(self.date_joined).humanize()

    def __str__(self):
        return self.email
