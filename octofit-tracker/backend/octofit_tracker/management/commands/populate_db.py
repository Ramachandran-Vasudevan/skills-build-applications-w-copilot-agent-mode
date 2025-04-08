from pymongo import MongoClient
from bson import ObjectId
from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        db.users.insert_many([
            {"_id": ObjectId(), **user} for user in test_data['users']
        ])

        db.teams.insert_many([
            {"_id": ObjectId(), **team} for team in test_data['teams']
        ])

        # Insert test data with unique activity_id
        db.activity.insert_many([
            {"_id": ObjectId(), "activity_id": ObjectId(), **activity} for activity in test_data['activities']
        ])

        # Insert test data with unique leaderboard_id
        db.leaderboard.insert_many([
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), **entry} for entry in test_data['leaderboard']
        ])

        # Insert test data with unique workout_id
        db.workouts.insert_many([
            {"_id": ObjectId(), "workout_id": ObjectId(), **workout} for workout in test_data['workouts']
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
