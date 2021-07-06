import constants
from csv import reader
import random
import os
import configparser


def import_csv_file(filename: str) -> list:
    """
    Imports a csv file with headers and returns each row as a list. The csv
    file must contain the headers (chore, frequency, description)

    :param filename: `String` of the path of where the csv file is located
    :return: The list of the rows in the csv file.
    """
    if not os.path.exists(filename):
        file = open(filename, 'w+')
        file.write(f"{constants.CSV_HEADERS}\n")
        file.write(f"{constants.CSV_DEFAULT_ROW}\n")

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


def get_task_list(chores: list, num_chores: int) -> list:
    """
    Randomly selects `num_chores` number of tasks based upon the input
    list chores. The frequency of chores also changes the likelihood that
    the chore is selected.

    :param chores: List of chores (Chore name, Frequency)
    :param num_chores: How many chores to be returned in the list
    :return: List of chores
    """
    chores.sort(key=lambda z: int(z[1]), reverse=True)

    chore_names = []
    weights = []
    for chore in chores:
        chore_names.append(chore[0])
        weight = 1 / float(chore[1])
        chore.append(weight)
        weights.append(weight)

    generated_chores = []
    chore_copy = []
    if len(chores) < num_chores:
        print("More chores are requested than are in list. Chores will "
              "be duplicated.")
        chore_copy = chores.copy()
    while len(generated_chores) < num_chores:
        choice = random.choices(chore_names, weights=weights).pop()
        if choice not in generated_chores or len(generated_chores) >= len(
                chores):
            generated_chores.append(choice)
        for index, chore in enumerate(chores):
            if choice == chore[0]:
                chores.remove(chore)
                break
        if len(chores) == 0:
            chores = chore_copy.copy()
    return generated_chores


def import_config(filename: str) -> None:
    if not os.path.exists(filename):
        print("'{}' not found. Creating default".format(filename))
        config_file = open(filename, 'w')

        config = configparser.ConfigParser()
        config.add_section('General')
        config.set('General', 'chores_to_generate', '1')
        config.set('General', 'csv_filename', 'chore_list.csv')

        config.write(config_file)
        config_file.close()

    with open(filename, 'r') as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_file(file)

    constants.NUM_CHORES = config.getint('General', 'chores_to_generate')
    constants.CHORE_LIST_CSV_NAME = config.get('General', 'csv_filename')
