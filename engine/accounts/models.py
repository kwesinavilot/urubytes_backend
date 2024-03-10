from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# create the organization model
class Organization(models.Model):
    orgID = models.CharField(_('Organization ID'), max_length=15)
    name = models.CharField(_('Organization Name'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    phoneNumber = models.CharField(_('Phone Number'), max_length=15)
    industry = models.CharField(_('Industry'), max_length=80)
    size = models.CharField(_('Organization Size'), max_length=10)
    country = models.CharField(_('Country'), max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.orgID} - {self.name} - Active: {self.is_active} - Date Created: {self.date_created}"

# Create user model
class User(AbstractBaseUser, PermissionsMixin):
    orgID = models.OneToOneField(Organization, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_('Full Name'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    phoneNumber = models.CharField(_('Phone Number'), max_length=15)
    role = models.CharField(_('Role'), max_length=80)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects: UserManager = UserManager()

    def __str__(self):
        return f"{self.name} - ({self.orgID}) - {self.email} - {self.phoneNumber} - superuser: {self.is_superuser} - active: {self.is_active} - joined: {self.date_joined}"
    
    def tokens(self):
        pass

# create the insights table
class Insight(models.Model):
    INTEREST = [
        ('1', "I'm researching startups for investment"),
        ('2', "I'm looking for insights on VC firms"),
        ('3', "I'm a startup founder seeking insights and resources"),
        ('4', "I'm an industry professional following startup and VC trends"),
    ]

    REFERER = [
        ('friend', "Through a friend"),
        ('industry', "Industry publication/conference"),
        ('social_media', "Social media"),
        ('networking', "Webinar/Networking event")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interests = models.CharField(_('Interest'), max_length=1, choices=INTEREST)
    referrer = models.CharField(_('Referrer'), max_length=15, choices=REFERER)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.interests} - {self.referrer} - {self.date_created}"