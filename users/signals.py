from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import User, UserProfile
from django.core.mail import send_mail



@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        # Create a profile for the user
        UserProfile.objects.create(user=instance)
    else:
        # Update the user's profile
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except UserProfile.DoesNotExist:
            # If the profile does not exist, create it
            UserProfile.objects.create(user=instance)
            
            
            # send_mail(
            #     subject='Welcome to Our Platform',
            #     message=f'Hello {instance.username}, your profile has been created successfully.',
            # )
          
#presave
@receiver(pre_save, sender=User)
def pre_save_create_profile_receiver(sender, instance, **kwargs):
    print(instance.username, "is being saved")