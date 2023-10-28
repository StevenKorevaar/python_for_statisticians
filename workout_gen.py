# workout_gen.py
import random
import math

class Exercise():
    def __init__(self, body_parts, rep_ranges=["1..3", "4..6", "7..9", "10..12"]):
        self.body_parts = body_parts
        self.rep_ranges = rep_ranges

body_part_reqs = [
    "chest",
    "triceps",
    "biceps",
    
    "front deltoids",
    "side deltoids",
    "rear deltoids",

    "upper back",
    "lats",
    "lower back",

    "quads",
    "hamstrings",
    "glutes"
]


major_muscle_groups = {
    "push": ["chest", "triceps", "front deltoids"],
    "pull": ["upper back", "lower back", "lats"],
    "legs": ["quads", "hamstrings", "glutes"]
}

import json
def read_exercises(filepath):
    exercises = {}
    f = json.load(open(filepath))
    # print(f)
    for exe in f["exercises"]:
        for e in exe:
            # print(e)
            # print(exe[e])
            exercises[e] = Exercise(exe[e][0]['body_parts'], exe[e][0]['rep_ranges'])
    return exercises

exercises = read_exercises("exercise_list.json")
# print(exercises)
# print(list(exercises.keys()))

def check_reqs(hit):
    for body_part in body_part_reqs: 
        if hit[body_part] <= 0: return False
    return True

def make_workout():
    hit = {}
    chosen_exercises = []
    for body_part in body_part_reqs: hit[body_part] = 0

    while not check_reqs(hit):
        chosen_exercise = random.choice(list(exercises.keys()))
        if chosen_exercise not in chosen_exercises:
            chosen_exercises.append(chosen_exercise)
            # print(chosen_exercise)
            # print(exercises[chosen_exercise])
            for bp in exercises[chosen_exercise].body_parts: hit[bp] += 1
        # else:
            # print("Already done", chosen_exercise)
    
    return chosen_exercises, hit

def break_into_sessions(exercise_list, num_sessions):
    assert num_sessions <= len(exercise_list)
    sessions = []
    exes_per_session = math.ceil(len(exercise_list) / num_sessions)
    print("exes_per_session", exes_per_session)
    for i in range(num_sessions):
        sess = []
        for j in range(exes_per_session):
            try:
                exe = random.choice(exercise_list)
                exercise_list.remove(exe)
                sess.append(exe)
            except:
                print("Finished exercises!")
                break
        sessions.append(sess)

    return sessions

exercise_list, body_parts_hit = make_workout()
print("\nChosen Exercises:")
print(exercise_list)

print("\nBody parts hit: ")
print(body_parts_hit)

sessions = break_into_sessions(exercise_list, 4)

print()
i = 0
for session in sessions:
    print(f"Session {i}:", session)
    print()
    i += 1 
