# workout_gen.py
import random
import math

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

exercises = {
    "bench press": ["chest", "triceps", "front deltoids"],
    "overhead press": {"triceps", "front deltoids", "side deltoids"},
    "tricep extensions": {"triceps"},
    "chest flies": {"chest"},

    "squat": {"quads", "hamstrings","glutes"},

    "deadlift": {"lower back", "hamstrings", "quads", "glutes", "upper back", "lats"},

    
    "pull up": {"lats", "upper back", "biceps"},
    "barbell row": {"lats", "upper back", "lower back", "rear deltoids"},
    "dumbbell row": {"lats", "upper back", "lower back", "rear deltoids"},

    "bicep curl": {"biceps"},
    "chin up": {"biceps", "lats"},


}

def check_reqs(hit, chosen_exercises):
    for body_part in body_part_reqs: 
        if hit[body_part] <= 0: return False
    return True

def make_workout():
    hit = {}
    chosen_exercises = []
    for body_part in body_part_reqs: hit[body_part] = 0

    while not check_reqs(hit, chosen_exercises):
        chosen_exercise = random.choice(list(exercises.keys()))
        if chosen_exercise not in chosen_exercises:
            chosen_exercises.append(chosen_exercise)
            # print(chosen_exercise)
            # print(exercises[chosen_exercise])
            for bp in exercises[chosen_exercise]: hit[bp] += 1
        # else:
            # print("Already done", chosen_exercise)
    
    return chosen_exercises

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

exercise_list = make_workout()
print("\nChosen Exercises:")
print(exercise_list)

sessions = break_into_sessions(exercise_list, 4)

print()
i = 0
for session in sessions:
    print(f"Session {i}:", session)
    print()
    i += 1 
