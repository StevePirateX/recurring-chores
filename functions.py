import constants
from csv import reader
import random


def import_csv_file(filename: str) -> list:
    file = open(filename, 'r')
    dt = reader(file)
    data = list(dt)
    file.close()
    rows = []
    for index, item in enumerate(data):
        if index > 0:
            item[1] = int(item[1])
            rows.append(item)
    return rows


def get_task_list(chores: list):
    chores.sort(key=lambda z: int(z[1]), reverse=True)

    chore_names = []
    weights = []
    for chore in chores:
        chore_names.append(chore[0])
        weight = 1 / float(chore[1])
        chore.append(weight)
        weights.append(weight)

    generated_chores = [random.choices(chore_names, weights=weights).pop()]
    while len(generated_chores) < constants.NUM_CHORES:
        choice = random.choices(chore_names, weights=weights).pop()
        if choice not in generated_chores:
            generated_chores.append(choice)
    return generated_chores
