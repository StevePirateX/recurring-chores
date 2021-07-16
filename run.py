import constants as c
import functions as f


def get_random_chores(chore_list: list, number_of_chores: int) -> None:
    """
    Function to generate the chore list. If the chore file doesn't
    exist, a default csv is created

    :return: None
    """
    selected_chores = f.get_task_list(chore_list, number_of_chores)
    print(f"Generated chores = ", end="")
    reset = "\u001B[0m"
    bold = "\u001B[1m"
    green = "\u001B[32m"
    for index, value in enumerate(selected_chores):
        formatted_value = bold + green + value + reset
        if index < len(selected_chores) - 1:
            print(formatted_value, end=", ")
        else:
            print(formatted_value)


if __name__ == '__main__':
    print("Welcome to Recurring Chores v{}".format(c.VERSION))
    f.import_config('config.ini')

    print("Running recurring chores...")
    chores = f.import_csv_file(c.CHORE_LIST_CSV_NAME)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i + 1}: {chore.get_name()} ({chore.get_frequency()})",
                  end="\t")
        print()
    get_random_chores(chores, c.NUM_CHORES)
    if c.TEST_MODE:
        for i in range(100):
            get_random_chores(chores, c.NUM_CHORES)
    else:
        while True:
            entry = input(
                "Press ENTER to generate a new set of chores... (q: quit): ")
            if entry != "":
                break
            get_random_chores(chores, c.NUM_CHORES)
