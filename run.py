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
    for index, value in enumerate(selected_chores):
        if index < len(selected_chores) - 1:
            print(value, end=", ")
        else:
            print(value)


if __name__ == '__main__':
    print("Welcome to Recurring Chores v{}".format(c.VERSION))
    print("Running recurring chores...")
    chores = f.import_csv_file(c.CHORE_LIST_CSV_NAME)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i + 1}: {chore[0]} ({chore[1]})", end="\t")
        print()
    get_random_chores(chores, c.NUM_CHORES)
    while True:
        entry = input(
            "Press ENTER to generate a new set of chores... (q: quit): ")
        if entry != "":
            break
        get_random_chores(chores, c.NUM_CHORES)
