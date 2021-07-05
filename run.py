import constants as c
import functions as f


def generate_chores():
    chore_list = f.get_task_list(chores)
    print(f"Generated chores = ", end="")
    for index, value in enumerate(chore_list):
        if index < len(chore_list) - 1:
            print(value, end=", ")
        else:
            print(value)


if __name__ == '__main__':
    print("Running recurring chores...")
    chores = f.import_csv_file(c.CHORE_LIST_CSV_NAME)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i + 1}: {chore[0]} ({chore[1]})", end="\t")
        print()
    generate_chores()
    while True:
        entry = input(
            "Press ENTER to generate a new set of chores... (q = quit): ")
        if entry != "":
            break
        generate_chores()
