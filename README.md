# Recurring Chores

![Version](https://img.shields.io/github/v/release/stevepiratex/recurring-chores?include_prereleases)
![License: MIT](https://img.shields.io/github/license/stevepiratex/recurring-chores)
![Python Version](https://img.shields.io/github/pipenv/locked/python-version/stevepiratex/recurring-chores)
![Language](https://img.shields.io/github/languages/top/stevepiratex/recurring-chores)

Randomly generates chores based on a pre-defined list

It takes a file input with the tasks, frequency (how often the task
should be completed) and any notes on how to accomplish the task.

When someone wants to have a list of chores, it will generate a list
of the specified number of tasks (e.g. 3 tasks) that someone wants to
do. This may be for them to complete over a week, within a given day
etc. If they don't like the selection, they just re-generate another
list.

### CSV Input File
The CSV file is formatted like so:

`Chore,Frequency (every x days),Description`

Description is not yet implemented.

### Config File

The `config.ini` contains two variables that can be changed:
- The CSV file name
- Number of chores to generate

If the file does not exist, it is created.