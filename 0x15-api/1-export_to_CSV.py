#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={"userId": argv[1]})
    users = requests.get("https://jsonplaceholder.typicode.com/users/",
                         params={"id": argv[1]})
    tasks = todos.json()
    user = users.json()
    for item in user:
        name = item.get("name")
        username = item.get('username')

    end_tasks = 0
    for task in tasks:
        if task.get("completed"):
            end_tasks += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, end_tasks, len(tasks)))
    for title in tasks:
        if title.get("completed"):
            print(title.get("title"))

    with open('{}.csv'.format(argv[1]), 'w') as f:
        data_file = task.get('title')
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1],
                             username,
                             task.get("completed"),
                             task.get("title")])
