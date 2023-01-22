import constants
from csv import reader
import random
import os
import configparser
from chore import Chore


def get_csv_file(csv_filename: str) -> list:
    """
    Imports a csv file with headers and returns each row as a list. The csv
    file must contain the headers (chore, frequency, description)

    :param csv_filename: `String` of the path of where the csv file is located
    :return: The list of the rows in the csv file.
    """
    if not os.path.exists(csv_filename):
        csv_file = open(csv_filename, 'w+')
        csv_file.write(f"{constants.CSV_HEADERS}\n")
        csv_file.write(f"{constants.CSV_DEFAULT_ROW}\n")

    csv_file = open(csv_filename, 'r')
    csv_file_data = reader(csv_file)
    chore_list = list(csv_file_data)
    csv_file.close()
    rows = []
    for chore_index, chore in enumerate(chore_list):
        if chore_index > 0:
            name = chore[0]
            frequency = int(chore[1])
            description = chore[2]
            chore = Chore(name, frequency, description)
            rows.append(chore)
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
    chore_names = []
    chore_weights = []
    for chore in chores:
        chore_names.append(chore.get_name())
        chore_weights.append(chore.get_weight())

    chosen_chores = []
    chore_copy = []
    if len(chores) < num_chores:
        print("More chores are requested than are in list. Chores will "
              "be duplicated.")
        chore_copy = chores.copy()
    while len(chosen_chores) < num_chores:
        choice = random.choices(chore_names, weights=chore_weights)
        choice_name = choice.pop()
        if choice_name not in chosen_chores or len(chosen_chores) >= len(
                chores):
            chosen_chores.append(choice_name)
        for index, chore in enumerate(chores):
            if choice == chore.get_name():
                chores.remove(chore)
                break
        if len(chores) == 0:
            chores = chore_copy.copy()
    return chosen_chores


def import_config(config_filename: str) -> None:
    """
    Imports the .ini file specified and sets the constants.
    :param config_filename: String of the csv_filename of the csv. The file
        is to be located in the same folder as the python file.
    :return: None
    """
    create_default_config(config_filename) if not os.path.exists(config_filename) else None

    with open(config_filename, 'r') as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_file(file)

    if config.has_option('General', 'chores_to_generate'):
        constants.NUM_CHORES = config.getint('General', 'chores_to_generate')
    if config.has_option('General', 'csv_filename'):
        constants.CHORE_LIST_CSV_PATH = config.get('General', 'csv_filename')
    if config.has_option('Test Mode', 'test_mode'):
        constants.test_mode = config.getboolean('Test Mode', 'test_mode')
    if config.has_option('Test Mode', 'iterations'):
        constants.test_iterations = config.getint('Test Mode', 'iterations')


def create_default_config(config_filename: str) -> None:
    print("'{}' not found. Creating default".format(config_filename))
    config_file = open(config_filename, 'w')

    config = configparser.ConfigParser()
    config.add_section('General')
    config.set('General', 'chores_to_generate', '1')
    config.set('General', 'csv_filename', 'chore_list.csv')
    config.add_section('Test Mode')
    config.set('Test Mode', 'test_mode', 'no')
    config.set('Test Mode', 'iterations', '10000')

    config.write(config_file)
    config_file.close()
