# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth import update_session_auth_hash
from progress.models import DailyGoalTracker, UserProgress, MindfulnessProgress
from challenges.models import BrainGame
from mindfulness.models import MindfulnessExercise
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from datetime import date
from django.conf import settings

def landing_page(request):
    return render(request, 'accounts/landing.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically login after registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('landing')  # change to your home url name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('landing')  # change to your home url name
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.bio = request.POST.get('bio')
        request.user.daily_goal = request.POST.get('daily_goal')
        request.user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    return render(request, 'accounts/edit_profile.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})



@login_required
def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('landing')
    return render(request, 'accounts/delete_account.html')



@login_required
def dashboard_view(request):
    user = request.user

    # Daily goal & streak data
    tracker = DailyGoalTracker.objects.filter(user=user).first()

    # Game progress
    total_games = BrainGame.objects.count()
    completed_games = UserProgress.objects.filter(user=user).count()
    game_progress_percent = int((completed_games / total_games) * 100) if total_games > 0 else 0

    # Mindfulness progress
    total_exercises = MindfulnessExercise.objects.count()
    completed_exercises = MindfulnessProgress.objects.filter(user=user).count()
    mindfulness_progress_percent = int((completed_exercises / total_exercises) * 100) if total_exercises > 0 else 0

    context = {
        'tracker': tracker,
        'total_games': total_games,
        'completed_games': completed_games,
        'game_progress_percent': game_progress_percent,
        'total_exercises': total_exercises,
        'completed_exercises': completed_exercises,
        'mindfulness_progress_percent': mindfulness_progress_percent,
    }
    return render(request, 'accounts/dashboard.html', context)



@csrf_protect
def forgot_password_view(request):
    User = get_user_model()

    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(username=username)
            user.password = make_password(new_password)
            user.save()
            messages.success(request, 'Password reset successfully.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Username not found.')

    return render(request, 'accounts/forgot_password.html')


@login_required
def profile_view(request):
    current_year = date.today().year
    joined_year = request.user.date_joined.year
    years_with_us = current_year - joined_year

    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'years_with_us': years_with_us,
    })



import razorpay
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        if not name or not amount:
            return render(request, "accounts/error.html", {"message": "Invalid form data"})

        amount_paise = int(amount) * 100

        payment = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1
        })

        return render(request, "accounts/payment_checkout.html", {
            "payment": payment,
            "amount": amount,
            "name": name,
            "key_id": settings.RAZORPAY_KEY_ID
        })
    return render(request, "accounts/payment_form.html")


def payment_checkout(request):
    return render(request, "accounts/payment_checkout.html")

def payment_success(request):
    return render(request, "accounts/payment_success.html")

def payment_error(request):
    return render(request, "accounts/error.html", {"message": "Payment failed. Please try again."})
