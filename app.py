FILE_NAME = "shopping_list.txt"


def add_item(item):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"[ ] {item}\n")


def show_list():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()
        print(content if content else "Lista jest pusta.")


def mark_as_bought(item_name):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if line.strip() == f"[ ] {item_name}":
            updated_lines.append(f"[x] {item_name}\n")
        else:
            updated_lines.append(line)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)


def main():
    while True:
        print("\n1 - Dodaj produkt")
        print("2 - Pokaż listę")
        print("3 - Oznacz jako kupiony")
        print("4 - Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            item = input("Podaj nazwę produktu: ")
            add_item(item)
        elif choice == "2":
            show_list()
        elif choice == "3":
            item = input("Podaj nazwę kupionego produktu: ")
            mark_as_bought(item)
        elif choice == "4":
            break
        else:
            print("Niepoprawna opcja.")


if __name__ == "__main__":
    main()