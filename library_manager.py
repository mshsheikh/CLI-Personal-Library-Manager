import json
import os

LIBRARY_FILE = "library.txt"

def load_library():
    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except:
        return []

def save_library(library):
    try:
        with open(LIBRARY_FILE, 'w') as file:
            json.dump(library, file, indent=4)
        print("\n✅ Library saved!")
    except:
        print("❌ Save failed!")

def add_book(library):
    print("\n📚 Add Book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    
    while True:
        year = input("Publication Year: ")
        if year.isdigit():
            break
        print("❌ Please enter numbers only")
    
    genre = input("Genre: ").strip()
    read = input("Read? (y/n): ").strip().lower() in ['y', 'yes']
    
    library.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read
    })
    print("✅ Book successfully added!")

def remove_book(library):
    title = input("\n🗑️ Remove Book - Enter title: ").lower()
    original_length = len(library)
    library[:] = [b for b in library if b["title"].lower() != title]
    
    if len(library) < original_length:
        print("✅ Book successfully removed!")
    else:
        print("❌ Book not found")

def search_books(library):
    print("\n🔍 Search")
    choice = input("1. Title\n2. Author\n> ")
    term = input("Search term: ").lower()
    
    if choice == '1':
        results = [b for b in library if term in b['title'].lower()]
    elif choice == '2':
        results = [b for b in library if term in b['author'].lower()]
    else:
        print("❌ Invalid choice")
        return
    
    if results:
        print("\nResults:")
        for i, b in enumerate(results, 1):
            print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {'Read' if b['read'] else 'Unread'}")
    else:
        print("❌ No matches")

def show_library(library):
    print("\n📖 Your Library")
    if not library:
        print("No books yet!")
        return
    
    for i, b in enumerate(library, 1):
        print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {'Read' if b['read'] else 'Unread'}")

def show_stats(library):
    total = len(library)
    if total == 0:
        print("❌ No books to show")
        return
    
    read = sum(1 for b in library if b['read'])
    print(f"\n📊 Stats:\nTotal: {total}\nRead: {read}\nUnread: {total - read}\nCompletion: {read/total*100:.0f}%")

def main():
    library = load_library()
    
    while True:
        print("\n📚 BooksLab: Your Personal Library Manager")
        print("1. Add Book\n2. Remove Book\n3. Search\n4. View All\n5. Stats\n6. Exit")
        print("Made with ❤  by mshsheikh")
        
        choice = input(">> Enter your choice here: ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            show_library(library)
        elif choice == '5':
            show_stats(library)
        elif choice == '6':
            save_library(library)
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()