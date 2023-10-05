from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)

class Usuario(AbstractBaseUser):
    id_usuario= models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dpi = models.CharField(max_length=13, unique=True)
    genero = models.CharField(max_length=255)
    escolaridad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=75)
    direccion = models.CharField(max_length=255)
    etnia = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    password = models.CharField(max_length=100) 
    

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'