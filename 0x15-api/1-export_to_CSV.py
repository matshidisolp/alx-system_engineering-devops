#!/usr/bin/python3
"""Gather data from an API and export TODO list progress
to CSV for a given employee ID."""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    emp_name = user_data.get("username")

    with open(f"{emp_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                emp_id, emp_name, task.get("completed"), task.get("title")
            ])
