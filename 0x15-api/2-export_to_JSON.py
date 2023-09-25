#!/usr/bin/python3
""" Python script to export data in JSON format. """
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={"user_id": argv[1]})
    users = requests.get("https://jsonplaceholder.typicode.com/users/",
                         params={"user_id": argv[1]})
    tasks = todos.json()
    user = users.json()
    for item in user:
        name = item.get("name")
        username = item.get("username")

    task_end = 0
    for task in tasks:
        if task.get("completed"):
            task_end += 1

    with open('{}.json'.format(argv[1]), 'w') as file:
        json_format = {}
        info_list = []
        for task in tasks:
            all_tasks = {}
            all_tasks['task'] = task.get("title")
            all_tasks['completed'] = task.get("completed")
            all_tasks['username'] = username
            info_list.append(all_tasks)
        json_format[argv[1]] = info_list
        json_obj = json.dumps(json_format)
        file.write(json_obj)
