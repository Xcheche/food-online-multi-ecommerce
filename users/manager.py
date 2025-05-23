from django.contrib.auth.models import BaseUserManager


#ALways 2
class UserManager(BaseUserManager):
    """
    Custom user manager for User model
    """
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
#creating superuser
    def create_superuser(self,first_name,last_name,username,email,password=None):
        """
        Create and return a superuser with an email, username and password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
      
    