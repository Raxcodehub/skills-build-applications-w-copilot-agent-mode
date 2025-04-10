from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        try:
            # Create test users
            user1, created = User.objects.get_or_create(
                email="user1@example.com", 
                defaults={"name": "User One", "password": "password1"}
            )
            user2, created = User.objects.get_or_create(
                email="user2@example.com", 
                defaults={"name": "User Two", "password": "password2"}
            )

            # Create test teams
            team1, created = Team.objects.get_or_create(name="Team Alpha")
            team2, created = Team.objects.get_or_create(name="Team Beta")

            # Add users to teams
            team1.members.add(user1)
            team2.members.add(user2)

            # Create test activities
            Activity.objects.get_or_create(
                user=user1, 
                defaults={"description": "Running 5km", "date": "2025-04-10T08:00:00Z"}
            )
            Activity.objects.get_or_create(
                user=user2, 
                defaults={"description": "Cycling 10km", "date": "2025-04-10T09:00:00Z"}
            )

            # Create test leaderboard entries
            Leaderboard.objects.get_or_create(team=team1, defaults={"score": 100})
            Leaderboard.objects.get_or_create(team=team2, defaults={"score": 80})

            # Create test workouts
            Workout.objects.get_or_create(
                name="Morning Yoga", 
                defaults={"description": "A 30-minute yoga session to start the day."}
            )
            Workout.objects.get_or_create(
                name="Evening Cardio", 
                defaults={"description": "A 45-minute cardio workout to end the day."}
            )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))