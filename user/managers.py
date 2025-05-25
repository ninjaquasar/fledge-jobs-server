from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email:str, password:str, **extra_fields):
        if not email or not password:
            raise ValueError("The Email and Password must be filled up.")
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email:str, password:str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError("A Superuser must have the staff permission")
        if not extra_fields.get('is_superuser'):
            raise ValueError("A Superuser must have the superuser permission")
        return self.create_user(email, password, **extra_fields)