#!/usr/bin/python3
"""Gather data from an API and display
TODO list progress for a given employee ID.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    emp_name = user_data.get("name")
    username = user_data.get("username")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]

    print(
        f"Employee {emp_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todos_data
    ]

    data = {str(emp_id): tasks}
    with open(f"{emp_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile)
