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
    def createUser(self, email, name, orgID, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.emailValidator(email)
        else:
            raise ValueError(_("Users must have an email address"))
        
        if not name:
            raise ValueError(_("Users must have a name"))
        
        if not orgID:
            raise ValueError(_("Users must have an organization ID"))

        user = self.model(email=email, name=name, orgID=orgID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def createAdminUser(self, email, name, orgID, password, **extra_fields):
        extra_fields.setdefault('isAdmin', True)

        if extra_fields.get('isAdmin') is not True:
            raise ValueError(_('Superuser must have isAdmin=True.'))
        
        user = self.createUser(email, name, orgID, password, **extra_fields)

        user.save(using=self._db)
        return user
    
