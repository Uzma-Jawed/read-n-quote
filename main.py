'''
This is the entry point of app. It will:
Load book and quote data
Show the main menu
Call functions from book_manager and quote_manager
Save data on each action
'''

from file_manager import load_data, save_data
import book_manager
import quote_manager

BOOKS_FILE = 'books.json'
QUOTES_FILE = 'quotes.json'

def main():
    books = load_data(BOOKS_FILE)
    quotes = load_data(QUOTES_FILE)

    while True:
        print("\n--- Personal Reading Journal ---")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search books")
        print("4. Update book")
        print("5. Delete a book")
        print("6. Add a quote")
        print("7. View all quotes")
        print("8. Search quotes")
        print("9. Delete a quote")
        print("10. Analysis")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        print(f"You chose: {choice}")

        if choice == '1':
            book_manager.add_book(books)
            save_data(BOOKS_FILE, books)
        elif choice == '2':
            book_manager.view_books(books)
        elif choice == '3':
            book_manager.search_books(books)
        elif choice == '4':
            book_manager.update_book(books)
            save_data(BOOKS_FILE, books)
        elif choice == '5':
            book_manager.delete_book(books)
            save_data(BOOKS_FILE, books)
        elif choice == '6':
            quote_manager.add_quote(quotes, books)
            save_data(QUOTES_FILE, quotes)
        elif choice == '7':
            quote_manager.view_quotes(quotes, books)
        elif choice == '8':
            quote_manager.search_quotes(quotes)
        elif choice == '9':
            quote_manager.delete_quote(quotes)
            save_data(QUOTES_FILE, quotes)
        elif choice == '10':
            print("\n--- Analysis Options ---")
            print("a. List books completed in a year")
            print("b. Book with most quotes")
            print("c. Author(s) with most entries")
            sub_choice = input("Choose (a/b/c): ").strip().lower()
            if sub_choice == 'a':
                book_manager.books_completed_in_year(books)
            elif sub_choice == 'b':
                quote_manager.book_with_most_quotes(quotes)
            elif sub_choice == 'c':
                book_manager.author_with_most_books(books)
            else:
                print("Invalid analysis option.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()