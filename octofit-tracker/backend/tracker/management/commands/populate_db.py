from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for fitness tracking'

    def handle(self, *args, **kwargs):
        self.stdout.write('Cleaning existing data from octofit_db...')
        
        # Clean up existing data
        Leaderboard.objects.all().delete()  # Delete leaderboard first due to foreign key constraints
        Activity.objects.all().delete()     # Delete activities due to foreign key constraints
        Team.objects.all().delete()         # Delete teams
        User.objects.all().delete()         # Delete users
        Workout.objects.all().delete()      # Delete workouts

        self.stdout.write('Creating test data for Octofit Tracker...')

        # Create test users with meaningful names and emails
        users = [
            User.objects.create(email="sarah.coach@merington.edu", name="Sarah Smith", password="secure123"),
            User.objects.create(email="mike.student@merington.edu", name="Mike Johnson", password="secure456"),
            User.objects.create(email="emily.student@merington.edu", name="Emily Brown", password="secure789"),
            User.objects.create(email="david.student@merington.edu", name="David Wilson", password="secure101"),
            User.objects.create(email="lisa.teacher@merington.edu", name="Lisa Anderson", password="secure202")
        ]

        # Create sports teams
        teams = [
            Team.objects.create(name="Track Stars"),
            Team.objects.create(name="Basketball Elite"),
            Team.objects.create(name="Swimming Champions"),
            Team.objects.create(name="Soccer United")
        ]

        # Add users to teams with meaningful distribution
        teams[0].members.add(users[0], users[1])  # Track team
        teams[1].members.add(users[2], users[3])  # Basketball team
        teams[2].members.add(users[1], users[4])  # Swimming team
        teams[3].members.add(users[2], users[3], users[4])  # Soccer team

        # Create various fitness activities with realistic data
        activities = [
            ("Track practice - 400m sprints", users[0]),
            ("Basketball shooting drills", users[2]),
            ("Freestyle swimming - 20 laps", users[1]),
            ("Soccer practice - penalty kicks", users[3]),
            ("Team cardio session", users[4]),
            ("Morning yoga routine", users[0]),
            ("Weight training", users[1]),
            ("Endurance running - 5km", users[2]),
            ("Team strategy session", users[3]),
            ("Cross-training workout", users[4])
        ]

        # Add activities with different dates
        for idx, (desc, user) in enumerate(activities):
            Activity.objects.create(
                user=user,
                description=desc,
                date=timezone.now() - timedelta(days=idx)
            )

        # Create leaderboard entries with meaningful scores
        leaderboards = [
            (teams[0], 850),  # Track Stars - high performance
            (teams[1], 780),  # Basketball Elite
            (teams[2], 920),  # Swimming Champions - top performers
            (teams[3], 800)   # Soccer United
        ]

        for team, score in leaderboards:
            Leaderboard.objects.create(team=team, score=score)

        # Create structured workout programs
        workouts = [
            ("Morning Fitness Routine", "30-minute program including stretching, jogging, and basic calisthenics."),
            ("Strength Training Program", "45-minute weight training focusing on major muscle groups."),
            ("Cardio Blast", "High-intensity interval training (HIIT) - 20 minutes of alternating sprints and recovery."),
            ("Team Sport Drills", "60-minute session of sport-specific exercises and team coordination drills."),
            ("Recovery Session", "Light stretching and mobility work, perfect for rest days."),
            ("Endurance Builder", "Long-distance running program with progressive distance goals."),
            ("Agility Training", "Quick footwork drills and reaction time exercises."),
            ("Core Strength Focus", "Ab workout routine with planks, crunches, and rotational exercises.")
        ]

        for name, desc in workouts:
            Workout.objects.create(name=name, description=desc)

        self.stdout.write(
            self.style.SUCCESS('Successfully cleaned and populated the database with test data for Octofit Tracker!')
        )