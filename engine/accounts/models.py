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
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.orgID

# Create user model
class User(AbstractBaseUser, PermissionsMixin):
    orgID = models.OneToOneField(Organization, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_('Full Name'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    phoneNumber = models.CharField(_('Phone Number'), max_length=15)
    role = models.CharField(_('Role'), max_length=80)
    isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'orgID']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        pass

# create the insights table
class Insights(models.Model):
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
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
