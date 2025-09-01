#!/usr/bin/env python3
"""
Sample queries demonstrating Django ORM relationships
"""

import os
import django
import sys

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for testing"""
    print("Creating sample data...")
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="City Library")
    
    # Add books to libraries
    library1.books.add(book1, book2)
    library2.books.add(book3)
    
    # Create librarians
    Librarian.objects.create(name="Sarah Johnson", library=library1)
    Librarian.objects.create(name="Michael Brown", library=library2)
    
    print("Sample data created successfully!\n")

def query_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def list_books_in_library(library_name):
    """
    List all books in a library
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")
        return None

def demonstrate_queries():
    """Demonstrate all required queries"""
    print("=" * 50)
    print("DEMONSTRATING DJANGO ORM RELATIONSHIP QUERIES")
    print("=" * 50)
    
    # Create sample data first
    create_sample_data()
    
    # 1. Query all books by a specific author
    print("1. Query all books by a specific author:")
    query_books_by_author("J.K. Rowling")
    print()
    
    # 2. List all books in a library
    print("2. List all books in a library:")
    list_books_in_library("Central Library")
    print()
    
    # 3. Retrieve the librarian for a library
    print("3. Retrieve the librarian for a library:")
    get_librarian_for_library("Central Library")
    print()

if __name__ == "__main__":
    demonstrate_queries()