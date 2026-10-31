from books import show_help, add_book, list_books, random_recommendation
catalog = []
show_help()
while True:
    command = input("Введите команду: ").strip()
    if command == "add_book":
        author = input("Введите автора: ").strip()
        title = input("Введите название книги: ").strip()
        if author == "" or title == "":
            print("Автор и название не могут быть пустыми.")
        else:
            add_book(catalog, author, title)
    elif command == "list_books":
        list_books(catalog)
    elif command == "random_recommendation":
        random_recommendation()
    elif command == "show_help":
        show_help()
    elif command == "exit":
        break
    else:
        print("Неизвестная команда. Введите show_help, чтобы увидеть список команд.")
