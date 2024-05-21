#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import requests


def numtask(todo):
    """get the totale number of task"""
    num = 0
    for task in todo.json():
        num += 1
    return num


def taskdone(todo):
    """get the number of task done"""
    done = 0
    for task in todo.json():
        if task.get("completed"):
            done += 1
    return done


def tasktitle(todo):
    """get the title"""
    title = []
    for task in todo.json():
        if task.get("completed"):
            title.append("\t" + task.get("title"))
    return title


def main():
    """main programe starting the sequence"""
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1])
    todos = requests.request("GET", url_todo)
    user = requests.request("GET", url_user)
    EMPLOYEE_NAME = user.json().get("name")
    NUMBER_OF_DONE_TASKS = taskdone(todos)
    TOTAL_NUMBER_OF_TASKS = numtask(todos)
    TASK_TITLE = tasktitle(todos)
    print("Employee {} is done with tasks({}/{})".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print(title)


if __name__ == "__main__":
    main()
