from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomLoginForm, UserUpdateForm, ProfileUpdateForm,CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"The account for {username} has been created. Please login")
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

@login_required
def profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid()  and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account profile updated')
            return redirect('profile')
    
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'profile.html', context)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordChangeForm