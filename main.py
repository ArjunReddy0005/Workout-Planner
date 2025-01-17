""" Workout Planner

This personal workout planner tracks workouts, progress and body training.
An organised plan determines which muscles are working out and if my efforts
are alligned with my fitness goals and muscle gain.
"""
__author__ = "Sai Arjun Reddy"
__docformat__ = 'reStructuredText'

import json
from datetime import datetime

WORKOUT_FILE = 'workout.json'
default_workouts = [
    {"workout_name": "Bench Press", "muscle_group": "Chest"},
    {"workout_name": "Squats", "muscle_group": "Legs"},
    {"workout_name": "Deadlift", "muscle_group": "Back"},
    {"workout_name": "Overhead Press", "muscle_group": "Shoulders"},
    {"workout_name": "Barbell Curl", "muscle_group": "Biceps"},
    {"workout_name": "Tricep Dips", "muscle_group": "Triceps"}
]


def main():
    """
    Entry point for the workout planner application.
    Provides a menu for the user to log workouts, get suggestions, and calculate progress.

    Args:
        None

    Returns:
        None

    Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(n)
    """

    begin_file()

    while True:
        
        print('Workout Out Planner\n')
        print('1. Log your workout')
        print('2. Suggest a workout')
        print('3. Calculate workout')
        print('4. Exit planner')
        
        option = input('Choose your option (number) to modify workout: ')

        if option == 1:
            print('Please enter the followings details:')
            
            muscleGroup = input("Muscle group: ")
            workoutName = input("Workout name: ")
            sets = input("Number of sets: ")
            reps = input("Number of reps: ")
            weights_kg = input('Weights (kg): ')

            log_workout(muscleGroup, workoutName, sets, reps, weights_kg)

        elif option == 2:
            print('Will generate workout:')
            generate_workout()
        elif option == 3:
            print('Will calculate estimated gains of current workout gain and total gain:')
            calculate_gains()
        elif option == 4:
            print('Exiting workout planner.')
            break
        else:
            print('Invalid option. Please choose options 1 - 4.')




