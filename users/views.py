from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
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
    return render(request, 'profile.html')