""" Workout Planner

This personal workout planner tracks workouts, progress and body training.
An organised plan determines which muscles are working out and if my efforts
are alligned with my fitness goals and muscle gain.
"""
__author__ = "Sai Arjun Reddy"
__docformat__ = '.py Python'

import json
from datetime import datetime

# File to store workout data
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
        Best Case Complexity: O(1), pick the exit option (4) to exit program and while loop.
        Worst Case Complexity: O(n), call a function or pick invalid option requiring multiple iterations within while loop.
    """

    begin_file()
    # Ensure file exists and is readable
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

def begin_file(): 
    
    """
    Ensures that the workout database file exists and is initialized.
    If the file is missing, it creates a new database with default structure.

    Args:
        None

    Returns:
        None

    Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        Best and worst case complexities are the same since the function will retun None after 1 iterations present
    """

    try:
        with open(WORKOUT_FILE, 'r') as workoutFile:
            workoutFile = json.load(workoutFile)
    except FileNotFoundError:
        with open(WORKOUT_FILE, 'w') as workoutFile:
            json.dump({'current_workout': [], 'past_workouts': []}, workoutFile, indent=5)
            
def log_workout(muscleGroup, workoutName, sets, reps, weights_kg):
    """
    Logs a workout entry into the database.

    Parameters:
        name (str): Name of the workout.
        muscle_group (str): Targeted muscle group.
        sets (int): Number of sets performed.
        reps (int): Number of repetitions per set.
        weight (float): Weight used during the workout (in kg).

    Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        Best and worst case complexities are the same since the function will retun None after 1 iterations present
    """
    entry = {
        'date': datetime.now().strftime("%d-/%m/%Y, %H:%M:%S"),
        'workout_name': workoutName,
        'muscle_group': muscleGroup,
        'Sets': sets,
        'Reps': reps,
        'Weights': weights_kg
    }

    with open(WORKOUT_FILE, 'r+') as workoutFile:
        workout_data = json.load(workoutFile)
        workout_data['past_workouts'].update(entry)
        workout_data['current_workout'].update(entry)

        workoutFile.seek()
        json.dump(workout_data,workoutFile,indent=5)

    print(f"{workoutName} targets the {muscleGroup}, completing {reps} reps for {sets} sets at a load of {weights_kg}.")

def generate_workout():
    """
    generates a workout by analyzing the least targeted muscle group in the workout history.

    Parameters: None
    Return: None

    Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        Best and worst case complexities are the same since the function will retun None after 1 iterations present.
    """
    with open(WORKOUT_FILE, 'r') as workoutFile:
            workoutFile = json.load(workoutFile)
        
    # Count occurrences of each muscle group in history
    muscle_count = {}
    for workout in workoutFile['past_workouts']:
        muscle_count[workout['muscle_group']] = muscle_count.get(workout['muscle_group'], 0) + 1
    
    # Find the least worked muscle group
    least_count_muscle = min(muscle_count, key=muscle_count.get)
    
    generate_workout = ''
    for workout in default_workouts:
        if workout['muscle_group'] == least_count_muscle:
            generated_workout = workout
    
    print(f'Suggested workout is {generated_workout['workout_name']} for the {generated_workout['muscle_group']}')

def calculate_gains():
    """
    Calculates the total weight lifted and estimates muscle gain based on workout history.

    Parameters: None
    Return: None

    Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        Best and worst case complexities are the same since the function will retun None after 1 iterations present

    """
    with open(WORKOUT_FILE, 'r') as workoutFile:
            workoutFile = json.load(workoutFile)

    tot_weigths = 0
    tot_muscle_gain = 0
    
    # Simplistic formula for muscle gain estimation
    muscle_gain_factor = 0.001

    # Iterate through past workouts in the history section of the json file and calculate total weights and muscle gain
    for entry in workoutFile['past_workouts']:
        # total weigths lifted += sets in each workout * reps * weigths
        tot_weigths += (entry['Sets'] *entry['Reps'] * entry['Weights'])
        # total muscle gain +=  sets in each workout * reps * weights * 0.001
        tot_muscle_gain += (entry['Sets'] *entry['Reps'] * entry['Weights']) * muscle_gain_factor
    
    print(f'Total weigth lifted is {tot_weigths}kg\nTotal muscle gain is {tot_muscle_gain}kg')



if __name__ == "__main__":
    main()


