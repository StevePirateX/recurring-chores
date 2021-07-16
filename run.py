import constants as c
import functions as f
import time


def get_random_chores(chore_list: list, number_of_chores: int, show_output: bool = True) -> None:
    """
    Function to generate the chore list. If the chore file doesn't
    exist, a default csv is created

    :return: None
    """
    selected_chores = f.get_task_list(chore_list, number_of_chores)
    if show_output:
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
    chores = f.import_csv_file(c.CHORE_LIST_CSV_NAME)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i + 1}: {chore.get_name()} ({chore.get_frequency()})",
                  end="\t")
        print()
    if c.TEST_MODE:
        time0 = time.time()
        iterations = 10000
        get_random_chores(chores, c.NUM_CHORES)         # To show the first output
        for i in range(iterations - 1):
            get_random_chores(chores, c.NUM_CHORES, False)
        time1 = time.time()
        run_time = time1 - time0
        print("Time ({} iterations) = {:.4f} secs".format(iterations, run_time))
    else:
        while True:
            get_random_chores(chores, c.NUM_CHORES)
            entry = input(
                "Press ENTER to generate a new set of chores... (q: quit): ")
            if entry != "":
                break
