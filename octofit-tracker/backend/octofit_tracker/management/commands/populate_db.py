from datetime import timedelta
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Debugging: Print user and team creation
        print(f"Created user: {user1}")
        print(f"Created user: {user2}")
        print(f"Created team: {team1}")

        # Debugging: Print activity creation
        activity1 = Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        activity2 = Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))
        print(f"Created activity: {activity1}")
        print(f"Created activity: {activity2}")

        # Debugging: Print leaderboard creation
        leaderboard1 = Leaderboard.objects.create(user=user1, score=150)
        leaderboard2 = Leaderboard.objects.create(user=user2, score=200)
        print(f"Created leaderboard entry: {leaderboard1}")
        print(f"Created leaderboard entry: {leaderboard2}")

        # Debugging: Print workout creation
        workout1 = Workout.objects.create(name='Push-ups', description='Do 20 push-ups')
        workout2 = Workout.objects.create(name='Sit-ups', description='Do 30 sit-ups')
        print(f"Created workout: {workout1}")
        print(f"Created workout: {workout2}")

        # Explicitly save objects to ensure they are committed to the database
        user1.save()
        user2.save()
        team1.save()
        activity1.save()
        activity2.save()
        leaderboard1.save()
        leaderboard2.save()
        workout1.save()
        workout2.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
