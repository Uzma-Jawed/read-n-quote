"""
This module will handle:
Adding a quote
Viewing all quotes
Searching by keyword
Deleting a quote
Showing the book with the most quotes
It will also use the normalize function from file_manager.py.
"""

from file_manager import normalize

def add_quote(quotes, books):
    book_title = input("Enter book title for the quote: ").strip()
    if not any(normalize(book['title']) == normalize(book_title) for book in books):
        print("This book is not in your journal.")
        return

    text = input("Enter the quote: ").strip()
    try:
        page = int(input("Enter page number: "))
    except ValueError:
        print("Invalid page number.")
        return

    quotes.append({
        "text": text,
        "book_title": book_title,
        "page": page
    })
    print("Quote added successfully.")

def view_quotes(quotes, books):
    print("\nQuotes sorted by book title:\n")
    for quote in sorted(quotes, key=lambda x: normalize(x['book_title'])):
        author = next((b['author'] for b in books if normalize(b['title']) == normalize(quote['book_title'])), 'Unknown')
        print(f"\"{quote['text']}\" - {quote['book_title']} by {author}, Page {quote['page']}")

def search_quotes(quotes):
    keyword = input("Enter keyword to search in quotes: ").strip().lower()
    results = [q for q in quotes if keyword in q['text'].lower()]
    for quote in results:
        print(f"\"{quote['text']}\" - {quote['book_title']}, Page {quote['page']}")

def delete_quote(quotes):
    text = input("Enter part of the quote to delete: ").strip().lower()
    matches = [i for i, q in enumerate(quotes) if text in q['text'].lower()]
    if not matches:
        print("Quote not found.")
        return
    for i in reversed(matches):
        print(f"Deleting: \"{quotes[i]['text']}\" from {quotes[i]['book_title']}")
        del quotes[i]
    print(f"Deleted {len(matches)} quote(s).")

def book_with_most_quotes(quotes):
    from collections import Counter
    book_counts = Counter([q['book_title'] for q in quotes])
    if book_counts:
        max_count = max(book_counts.values())
        top_books = [title for title, count in book_counts.items() if count == max_count]
        print(f"Book(s) with the most quotes: {', '.join(top_books)} ({max_count} quotes)")
    else:
        print("No quotes available.")