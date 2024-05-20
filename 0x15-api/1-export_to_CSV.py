#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys
import csv


if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        data_rows = [[user_id, username, i.get("completed"),
                      i.get("title")] for i in todos]
        writer.writerows(data_rows)
