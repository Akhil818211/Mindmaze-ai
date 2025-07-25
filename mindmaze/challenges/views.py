from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BrainGame
from django.contrib import messages
from progress.models import UserProgress, DailyGoalTracker
from datetime import date
from django.core.paginator import Paginator
from accounts.utils.profile_stats import update_user_stats



def game_list_view(request):
    games = BrainGame.objects.all()
    paginator = Paginator(games, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    completed_games = set()
    if request.user.is_authenticated:
        completed_games = set(
            UserProgress.objects.filter(user=request.user).values_list('game_id', flat=True)
        )

    return render(request, 'challenges/game_list.html', {
        'page_obj': page_obj,
        'completed_games': completed_games,
    })


@login_required
def play_game_view(request, game_id):
    game = get_object_or_404(BrainGame, id=game_id)

    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        if user_answer.strip().lower() == game.correct_answer.strip().lower():
            # Save progress only if not already completed
            progress, created = UserProgress.objects.get_or_create(user=request.user, game=game)
            if created:
                today = date.today()
                tracker, _ = DailyGoalTracker.objects.get_or_create(user=request.user)

                # ✅ Streak logic
                if tracker.last_completed == today:
                    pass  # already done today
                elif tracker.last_completed == today.fromordinal(today.toordinal() - 1):  # yesterday
                    tracker.current_streak += 1
                else:
                    tracker.current_streak = 1  # reset streak

                tracker.last_completed = today
                tracker.total_completed += 1
                tracker.save()

                # ✅ Update profile stats
                update_user_stats(request.user, game_completed=True)

            messages.success(request, "✅ Correct! Challenge completed.")
            return redirect('game_list')
        else:
            messages.error(request, "❌ Incorrect. Try again.")

    return render(request, 'challenges/play_game.html', {'game': game})
