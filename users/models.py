from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from common.models import BaseModel
from .manager import UserManager
# Create your models here.



#Abstractuser dosent add enough fields, thats why we use abstractbaseuser
class  User(BaseModel,AbstractBaseUser):
    RESTAURANT = 1
    
    CUSTOMER = 2
    ROLE_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer'),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    role  = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER,blank=True,null=True)
    
    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] #excluded phone number in required fields
 
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        # Simplest possible answer: Yes, always
        return True
class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures/%Y/%m/%d/', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        if self.user and hasattr(self.user, 'username') and self.user.username:
            return f"{self.user.username}'s Profile"
        return "User Profile without User"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'