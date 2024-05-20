#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""
import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists"""
    
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + "todos?userId={}".format(user_id)
        todo = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": user.get("username"),
            }
            for i in todo
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
