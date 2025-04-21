#Hala 
#- Create a dictionary for a workout named "Push-ups"
#- With the keys exercise, sets, reps and notes 
push_ups ={
    "exercise": "push-ups",
    "sets": 3,
    "reps": 10,
    "notes": "keep your back straight and core engaged"
}
#Accessing Dictionary keys
print(push_ups["exercise"])
print(push_ups["sets"])
print(push_ups["reps"])
print(push_ups["notes"])

#3. Accessing Dictionary keys

#- Update the sets of the exercise
#- Delete notes with del
#- Add the key back aw workout_notes with the same value that notes had
push_ups["sets"] = 4
del push_ups["notes"]
push_ups[" workout_notes"] = "keep your back straight and core engaged"
print(push_ups)


#4. Accessing nested data

# Add the nested dictionary below

workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}
#- Access Lunges notes

print(workout_plan["Lunges"]["notes"])


#5. Iterating over a dictionary

#- Copy and observe the solution code

# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.
for key, value in push_ups.items():
    print(f"{key.upper()}: {value}")



