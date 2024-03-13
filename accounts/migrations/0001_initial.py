# Generated by Django 5.0.3 on 2024-03-10 14:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('orgID', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Organization ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Organization Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('phoneNumber', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('industry', models.CharField(max_length=80, verbose_name='Industry')),
                ('size', models.CharField(max_length=10, verbose_name='Organization Size')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('isActive', models.BooleanField(default=True)),
                ('isVerified', models.BooleanField(default=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userID', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='User ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('phoneNumber', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('role', models.CharField(max_length=80, verbose_name='Role')),
                ('isAdmin', models.BooleanField(default=False, verbose_name='Is Admin')),
                ('isActive', models.BooleanField(default=True, verbose_name='Is Active')),
                ('dateJoined', models.DateTimeField(auto_now_add=True)),
                ('lastLogin', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('orgID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(choices=[('1', "I'm researching startups for investment"), ('2', "I'm looking for insights on VC firms"), ('3', "I'm a startup founder seeking insights and resources"), ('4', "I'm an industry professional following startup and VC trends")], max_length=1, verbose_name='Interest')),
                ('referrer', models.CharField(choices=[('friend', 'Through a friend'), ('industry', 'Industry publication/conference'), ('social_media', 'Social media'), ('networking', 'Webinar/Networking event')], max_length=15, verbose_name='Referrer')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]