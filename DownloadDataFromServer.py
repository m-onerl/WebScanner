"""pobieranie danych z serwera"""
"""

"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Błąd dekodowania JSON")
else:
    taskFrequency = {}
    for entry in tasks:
        if(entry["completed"] == True):
            if(entry["userId"] in taskFrequency):
                taskFrequency[entry["userId"]] += 1
            else:
                taskFrequency[entry["userId"]] = 1
print(taskFrequency)