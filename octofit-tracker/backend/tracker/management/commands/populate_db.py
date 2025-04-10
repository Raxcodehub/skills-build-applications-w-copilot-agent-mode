from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, description="Running 5km", date="2025-04-10T08:00:00Z")
        Activity.objects.create(user=user2, description="Cycling 10km", date="2025-04-10T09:00:00Z")

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=80)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A 30-minute yoga session to start the day.")
        Workout.objects.create(name="Evening Cardio", description="A 45-minute cardio workout to end the day.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
