# Recurring Chores

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
