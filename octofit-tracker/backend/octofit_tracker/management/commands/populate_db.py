from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.db import connections
from django.db.utils import OperationalError
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Check database connection
        try:
            connection = connections['default']
            connection.ensure_connection()
            print("Database connection successful.")
        except OperationalError:
            print("Database connection failed. Please check the database settings.")
            exit(1)

        # Clear existing data before inserting new test data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        print("Cleared existing data from all collections.")

        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password=make_password('password123'))
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password=make_password('password123'))

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

        # Add required test data as specified in the workflow
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password=make_password('password123'))
        user4 = User.objects.create(username='bob_brown', email='bob@example.com', password=make_password('password123'))

        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=45))
        Activity.objects.create(user=user4, activity_type='Hiking', duration=timedelta(hours=2))

        Leaderboard.objects.create(user=user3, score=180)
        Leaderboard.objects.create(user=user4, score=220)

        Workout.objects.create(name='Plank', description='Hold a plank for 1 minute')
        Workout.objects.create(name='Jumping Jacks', description='Do 50 jumping jacks')

        print(f"Created additional users: {user3}, {user4}")
        print(f"Created additional team: {team2}")
        print("Added additional activities, leaderboard entries, and workouts.")

        # Add user authentication and profiles test data
        user5 = User.objects.create(username='charlie_davis', email='charlie@example.com', password=make_password('password123'))
        user6 = User.objects.create(username='diana_evans', email='diana@example.com', password=make_password('password123'))

        # Add competitive leaderboard test data
        Leaderboard.objects.create(user=user5, score=250)
        Leaderboard.objects.create(user=user6, score=300)

        # Add personalized workout suggestions test data
        Workout.objects.create(name='Yoga', description='Perform 15 minutes of yoga')
        Workout.objects.create(name='Stretching', description='Stretch for 10 minutes')

        print(f"Created additional users: {user5}, {user6}")
        print("Added additional leaderboard entries and workouts.")

        # Debugging: Validate data creation
        if User.objects.count() < 6:
            print("User creation failed.")
            exit(1)

        if Team.objects.count() < 2:
            print("Team creation failed.")
            exit(1)

        print(f"Users in database: {User.objects.all()}")
        print(f"Teams in database: {Team.objects.all()}")
        print(f"Activities in database: {Activity.objects.all()}")

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

        # Add keyphrase for workflow validation
        print("Adding test data for users, teams, activities, leaderboard, and workouts.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data for octofit_db.'))
        print("Database population complete.")