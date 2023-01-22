import constants as c
import functions as f
import time


def get_random_chores(chore_list: list, number_of_chores: int, show_output: bool = True) -> None:
    """
    Function to generate the chore list. If the chore file doesn't
    exist, a default csv is created

    :return: None
    """
    randomly_selected_chores = f.get_task_list(chore_list, number_of_chores)
    if show_output:
        printed_title = f"Generated chore{'s' if c.NUM_CHORES > 1 else ''}"
        print(f"{printed_title} = ", end="")
        reset_format = "\u001B[0m"
        bold_format = "\u001B[1m"
        green_format = "\u001B[32m"
        for selected_chore_index, selected_chore in enumerate(randomly_selected_chores):
            formatted_chore = bold_format + green_format + selected_chore + reset_format
            if selected_chore_index < len(randomly_selected_chores) - 1:
                print(formatted_chore, end=", ")
            else:
                print(formatted_chore)


if __name__ == '__main__':
    print("Welcome to Recurring Chores v{}".format(c.VERSION))
    f.import_config('config.ini')
    chores = f.get_csv_file(c.CHORE_LIST_CSV_PATH)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i + 1}: {chore.get_name()} ({chore.get_frequency()})",
                  end="\t")
        print()
    if c.test_mode:
        time_start = time.time()
        get_random_chores(chores, c.NUM_CHORES)         # To show the first output
        for i in range(c.test_iterations - 1):
            get_random_chores(chores, c.NUM_CHORES, False)
        time_end = time.time()
        run_time = time_end - time_start
        print("Time ({} iterations) = {:.4f} secs".format(c.test_iterations, run_time))
    else:
        while True:
            get_random_chores(chores, c.NUM_CHORES)
            entry = input(
                "Press ENTER to generate a new set of chores... (q: quit): ")
            if entry != "":
                break
