import constants as c
import functions as f


if __name__ == '__main__':
    print("Running recurring chores...")
    chores = f.import_csv_file(c.CHORE_LIST_CSV_NAME)
    if c.PRINT_INPUT_CHORE_LIST:
        print("Chores: ", end="")
        for i, chore in enumerate(chores):
            print(f"{i+1}: {chore[0]} ({chore[1]})", end="\t")
        print()
    chore_list = f.get_task_list(chores)
    print(f"Generated chores = ", end="")
    for i, chore in enumerate(chore_list):
        if i < len(chore_list) - 1:
            print(chore, end=", ")
        else:
            print(chore)
    input("Press ENTER to exit ")
