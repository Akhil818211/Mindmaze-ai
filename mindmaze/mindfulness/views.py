from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MindfulnessExercise
from progress.models import MindfulnessProgress
from django.contrib import messages
from django.core.paginator import Paginator



@login_required
def exercise_list_view(request):
    all_exercises = MindfulnessExercise.objects.all()
    paginator = Paginator(all_exercises, 6)  # 6 exercises per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    completed = MindfulnessProgress.objects.filter(user=request.user).values_list('exercise_id', flat=True)

    return render(request, 'mindfulness/exercise_list.html', {
        'page_obj': page_obj,
        'completed': completed,
    })
@login_required
def exercise_detail_view(request, exercise_id):
    exercise = get_object_or_404(MindfulnessExercise, id=exercise_id)

    # Handle completion tracking
    if request.method == 'POST':
        MindfulnessProgress.objects.get_or_create(user=request.user, exercise=exercise)
        messages.success(request, "🧘 Exercise completed. Great job!")
        return redirect('exercise_list')

    return render(request, 'mindfulness/exercise_detail.html', {
        'exercise': exercise
    })


def mindfulness_list(request):
    return render(request, 'mindfulness/list.html')
