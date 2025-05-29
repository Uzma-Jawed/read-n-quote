# This module will handle:
# Adding a book, Viewing all books, Searching, Updating, Deleting, Book-related analysis
# It will use the helper functions from file_manager.py.

from file_manager import normalize

def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    if any(normalize(b['title']) == normalize(title) and normalize(b['author']) == normalize(author) for b in books):
        print("This book already exists.")
        return

    try:
        year = int(input("Enter year published: "))
    except ValueError:
        print("Invalid year.")
        return

    genres = set(g.strip() for g in input("Enter genres (comma-separated): ").lower().split(','))
    status = input("Enter status (reading/completed/on hold): ").strip().lower()
    if status not in ["reading", "completed", "on hold"]:
        print("Invalid status.")
        return
    
    books.append({
        "title": title,
        "author": author,
        "year": year,
        "genres": list(genres),
        "status": status
    })
    print("Book added successfully.")

def view_books(books):
    for book in sorted(books, key=lambda x: x['year']):
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['status'].capitalize()} - Genres: {', '.join(book['genres'])}")

def search_books(books):
    key = input("Search by genre or status: ").strip().lower()
    results = [b for b in books if key in b['genres'] or b['status'] == key]
    for book in results:
        print(f"{book['title']} by {book['author']}")

def update_book(books):

    title = input("Enter book title to update: ").strip()
    author = input("Enter author: ").strip()
    for book in books:
        if normalize(book['title']) == normalize(title) and normalize(book['author']) == normalize(author):
            choice = input("Update status or add genre? (status/genre): ").strip().lower()
            if choice == 'status':
                new_status = input("Enter new status: ").strip().lower()
                if new_status in ["reading", "completed", "on hold"]:
                    book['status'] = new_status
                    print("Status updated.")
                else:
                    print("Invalid status.")
            elif choice == 'genre':
                new_genres = set(g.strip() for g in input("Enter new genres (comma-separated): ").lower().split(','))
                book['genres'] = list(set(book['genres']) | new_genres)
                print("Genres updated.")
            return
    print("Book not found.")

def delete_book(books):
    title = input("Enter book title to delete: ").strip()
    author = input("Enter author: ").strip()
    for i, book in enumerate(books):
        if normalize(book['title']) == normalize(title) and normalize(book['author']) == normalize(author):
            del books[i]
            print("Book deleted.")
            return
    print("Book not found.")

def books_completed_in_year(books):
    try:
        year = int(input("Enter year: "))
        completed = [b for b in books if b['status'].lower() == 'completed' and b['year'] == year]
        if completed:
            for book in completed:
                print(f"{book['title']} by {book['author']}")
        else:
            print("No completed books found for that year.")
    except ValueError:
        print("Invalid year.")

def author_with_most_books(books):
    from collections import Counter
    author_counts = Counter([b['author'] for b in books])
    if author_counts:
        max_count = max(author_counts.values())
        top_authors = [author for author, count in author_counts.items() if count == max_count]
        print(f"Author(s) with most entries: {', '.join(top_authors)} ({max_count} books)")
    else:
        print("No books available.")