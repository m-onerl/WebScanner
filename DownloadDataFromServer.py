"""pobieranie danych z serwera"""
"""
def get_keys_with_top_values(my_dict):
    return[   
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]
"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    taskFrequency = {}
    for entry in tasks:
        if(entry["completed"] == True):
            if(entry["userId"] in taskFrequency):
                taskFrequency[entry["userId"]] += 1
            else:
                taskFrequency[entry["userId"]] = 1
    return taskFrequency

def get_keys_with_top_values(my_dict):
    return[   
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]

def user_with_most_completed(taskFrequency):
    userWithMost = []
    maxAmount = max(taskFrequency.values())
    for userId, numberOfCompleted in taskFrequency.items():
        if (numberOfCompleted == maxAmount):
            userWithMost.append(userId)
    return userWithMost

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Błąd dekodowania JSON")
else:
    taskFrequency = count_task_frequency(tasks)
    UsersWithTopCompleted = (user_with_most_completed(taskFrequency))


r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()
    
for user in users:
    if(user["id"] in UsersWithTopCompleted):
        print("Wreczamy nagrody dla użytkowników z id:", user["name"])