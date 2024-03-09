from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    # validate emails
    def emailValidator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))
    
    # create user
    def create_user(self, email, name, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.emailValidator(email)
        else:
            raise ValueError(_("Users must have an email address"))
        
        if not name:
            raise ValueError(_("Users must have a name"))
        
        # if not orgID:
        #     raise ValueError(_("Users must have an organization ID"))

        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        user = self.create_user(email, name, password, **extra_fields)

        user.save(using=self._db)
        return user
    
