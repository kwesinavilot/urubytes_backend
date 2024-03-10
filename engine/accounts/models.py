from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# create the organization model
class Organization(models.Model):
    orgID = models.CharField(_('Organization ID'), max_length=15, primary_key=True)
    name = models.CharField(_('Organization Name'), max_length=100, unique=True)
    email = models.EmailField(_('Email Address'), null=True, blank=True)
    phoneNumber = models.CharField(_('Phone Number'), max_length=15, null=True, blank=True)
    industry = models.CharField(_('Industry'), max_length=80)
    size = models.CharField(_('Organization Size'), max_length=10)
    country = models.CharField(_('Country'), max_length=50)
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['orgID','name']

    def __str__(self):
        return f"{self.orgID} - {self.name} - Active: {self.isActive} - Date Created: {self.dateCreated}"

# Create user model
class User(AbstractUser):
    username = None
    userID = models.CharField(_('User ID'), max_length=15, primary_key=True)
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(_('Full Name'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    phoneNumber = models.CharField(_('Phone Number'), max_length=15)
    role = models.CharField(_('Role'), max_length=80)
    isAdmin = models.BooleanField(_('Is Admin'), default=False)
    isActive = models.BooleanField(_('Is Active'), default=True)
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} - ({self.orgID}) - {self.email} - {self.phoneNumber} - superuser: {self.isAdmin} - active: {self.isActive} - joined: {self.dateJoined}"

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

    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insights')
    interests = models.CharField(_('Interest'), max_length=1, choices=INTEREST)
    referrer = models.CharField(_('Referrer'), max_length=15, choices=REFERER)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.userID} - {self.interests} - {self.referrer} - {self.dateCreated}"