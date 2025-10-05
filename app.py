import sqlite3
import os
DATABASE_FILE = 'books.db'

def connect_db():
    print("Connecting to the database...")
    return sqlite3.connect(DATABASE_FILE)

def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER ,
        is_read BOOLEAN 
        )
      ''')
    conn.commit()
    conn.close()
    print(f"Database setup complete. Table 'books' is created.")

def add_book(title, author, year, is_read):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
      INSERT INTO books (title, author, year, is_read)
      VALUES (?, ?, ?, ?)
      ''', (title, author, year, is_read))
    conn.commit()
    conn.close()
    print(f"Book '{title}' by {author} added to the database.")

def read_all_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    print("\n--- Book List ---")
    for book in books:
        status = "Read" if book[4] else "Not Read"
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Status: {status}")
    print("---------------------")
    return books

def mark_book_read(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
      UPDATE books
      SET is_read = 1
      WHERE id = ?
      ''', (book_id,))
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} marked as read.")
    if cursor.rowcount > 0:
        print(f"\n update {book_id}.")
    else:
        print(f"\n no update {book_id}.")

def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
      DELETE FROM books
      WHERE id = ?
      ''', (book_id,))
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} deleted from the database.")
    if cursor.rowcount > 0:
        print(f"\n delete {book_id}.")
    else:
        print(f"\n no delete {book_id}.")

def show_menu():
    print("\n--- books manager(CLI)---")
    print("1.add new book")
    print("2. show all books")
    print("3. mark a book as read")
    print("4. delete a book")
    print("5. exit")
    print("------------------------------\n")

def main_loop():
    setup_database()
    while True:
        read_all_books()
        show_menu()
        choice = input("choose options (1-5): ")
        if choice == '1':
            title = input("enter a book title: ")
            author = input("enter a book author: ")
            year = int(input("enter the year of publication: "))
            is_read = input("have you read the book? (y/n): ").lower() == 'y'
            add_book(title, author, year, is_read)
        elif choice == '2':
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books')
            books = cursor.fetchall()
            conn.close()
            print("\n book list:")
            for book in books:
                status = "was read" if book[4] else "not read yet"
                print(f"ID: {book[0]}, title: {book[1]}, author: {book[2]}, year: {book[3]}, status: {status}")
            print("")
        elif choice == '3':
            book_id = int(input("enter the book ID to marke as read: "))
            mark_book_read(book_id)
        elif choice == '4':
            book_id = int(input("enter the book ID to delete: "))
            delete_book(book_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("invaild selection , try again.")


if __name__ == '__main__':
    main_loop()