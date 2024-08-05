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

# 1 sposób
"""
r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()
    
for user in users:
    print(UsersWithTopCompleted)
    if(user["id"] in UsersWithTopCompleted):
        print("Wreczamy nagrody dla użytkowników :", user["name"])
"""

"""# 2 sposób
for userId in UsersWithTopCompleted:
    print(userId)
    #r = requests.get("https://jsonplaceholder.typicode.com//users?id=" + str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com//users?id=", params="id="+str(userId))
    user = r.json()
    for user in user:
        print("Wreczamy nagrody dla użytkowników :", user["name"]) 
"""
# 3 sposób

def change_list_into(my_list):
    conj_param = "id="
    for item in my_list:
        conj_param += str(item)
        if item != my_list[-1]:
            conj_param += "&id="
    return conj_param
 
conj_param = change_list_into(UsersWithTopCompleted)

r = requests.get("https://jsonplaceholder.typicode.com//users?id=", params=conj_param)
users = r.json()
for user in users:
    print("Wreczamy nagrody dla użytkowników :", user["name"])