from django.shortcuts import render
from .models import UserProgress

def user_progress_view(request):
    progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'progress/user_progress.html', {'progress': progress})
