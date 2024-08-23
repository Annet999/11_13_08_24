# test_library_manager.py

from library_manager import Library, generate_report

def main():
    # Создаем экземпляр библиотеки
    library = Library()

    # Добавляем книги
    library.add_book("1984", "George Orwell", "Dystopia")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")

    # Проверяем список всех книг
    print("Все книги в библиотеке:")
    print(generate_report(library))

    # Ищем книги по автору
    print("\nКниги, написанные George Orwell:")
    books_by_orwell = library.find_books_by_author("George Orwell")
    for book in books_by_orwell:
        print(f"Title: {book['title']}, Genre: {book['genre']}")

    # Удаляем книгу
    library.remove_book("1984")
    
    # Проверяем список всех книг после удаления
    print("\nВсе книги в библиотеке после удаления '1984':")
    print(generate_report(library))

if __name__ == "__main__":
    main()