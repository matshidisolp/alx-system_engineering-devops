#!/usr/bin/python3
"""Fetch and export TODO list of employees from an API to a JSON file."""

import json
import requests


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    users_dict = {user['id']: [{
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        } for task in todos if task['userId'] == user['id']] for user in users}

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
