from django.shortcuts import render,redirect

from users.forms import UserForm
from users.models import User

# Create your views here.


def home(request):
    return render(request,'users/home.html')


def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user.set_password(password)  # Hash the password before saving
            # Save the user data to the database
            user = form.save(commit=False)
            user_role = User.CUSTOMER  # Default role
            #or use cleaned data and create object to validate so to hash password 
            user.save()
            # Redirect to a success page or render a success message
            return redirect('home')  # Assuming you have a URL named 'home'
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request,'users/register_user.html', context)