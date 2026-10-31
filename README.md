import random
from books_data import RECOMMENDED_BOOKS
def show_help():
    print("add_book — добавить книгу")
    print("list_books — показать каталог")
    print("random_recommendation — случайная рекомендация")
    print("show_help — показать помощь")
    print("exit — выйти из программы")
def add_book(catalog, author, title):
    book = {"author": author, "title": title}
    catalog.append(book)
    print(f"Книга «{title}» добавлена в каталог.")
def list_books(catalog):
    if len(catalog) == 0:
        print("Каталог пуст.")
        return
    else:
        print("Ваш каталог книг:")
        print(catalog)
def random_recommendation():
    book = random.choice(RECOMMENDED_BOOKS)
    print("Рекомендую прочитать:")
    print(book)
