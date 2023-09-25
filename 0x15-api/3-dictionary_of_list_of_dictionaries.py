#!/usr/bin/python3
"""[Python script to export Records all tasks
    from all employees in the JSON format.]
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    users_req = {}
    todo_dict = {}
    for user in users:
        _id = user.get("id")
        username = user.get("username")
        todo_dict[_id] = []
        users_req[_id] = username

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in tasks:
        userId = task.get("userId")
        all_tasks = {}
        all_tasks['task'] = task.get("title")
        all_tasks['completed'] = task.get("completed")
        all_tasks['username'] = users_req.get(userId)
        todo_dict.get(userId).append(all_tasks)

    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_dict, file)
