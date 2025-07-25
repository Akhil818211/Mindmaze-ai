def update_user_stats(user_profile, correct, total):
    user_profile.challenges_completed += 1
    user_profile.total_attempts += total
    user_profile.total_correct += correct

    if user_profile.total_attempts > 0:
        user_profile.success_rate = round((user_profile.total_correct / user_profile.total_attempts) * 100, 2)

    user_profile.save()
