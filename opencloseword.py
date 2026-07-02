
import os
from datetime import datetime

JOURNAL_FILE = "journal.txt"


def write_entry():
    print("Enter your journal entry:")
    print("Press Enter on an empty line to finish.")

    lines = []

    while True:
        line = input("> ")
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("No entry was made.")
        return

    # Append (a) mode
    with open(JOURNAL_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write("\n============================\n")
        file.write(f"Entry Date: {timestamp}\n")
        file.write("============================\n")

        # Write the actual entry
        for line in lines:
            file.write(line + "\n")

        file.write("\n")

    print("Your entry has been saved to the journal.")


def read_journal():
    print("\n-- Reading your journal --")

    if not os.path.exists(JOURNAL_FILE):
        print("No journal entries found.")
        return

    # Open the file in read mode
    with open(JOURNAL_FILE, "r") as file:
        content = file.read()

        if content.strip() == "":
            print("Your journal file exists but is empty.")
        else:
            print(content)


def main():
    while True:
        print("\n===== Personal Journal App =====")
        print("1. Write a new journal entry")
        print("2. Read your journal")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_journal()
        elif choice == "3":
            print("Thank you for using the Journal App!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__== "__main__":
    main()