def main():
    print(f"🗼 running tracker")
    # Get user to input here expense
    get_user_expense()

    # write to file
    write_to_file()

    # read from file
    read_from_file()


def get_user_expense():
    print(f"get user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"you entered {expense_name}, {expense_amount}")

    expense_categories = ["food", "home", "work", "fun", "misc"]

    while True:
        print("select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"enter a cat num {value_range }: ")) - 1

        if selected_index in range(len(expense_categories)):
            break
        else:
            print("please enter good num")


def write_to_file():
    print(f"write to file")


def read_from_file():
    print(f"read from file")


if __name__ == "__main__":
    main()
