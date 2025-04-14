import streamlit as st
import json

LIBRARY_FILE = "library.json"

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library, title, author, year, genre, read_status):
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)
    save_library(library)

def remove_book(library, title):
    updated_library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(updated_library)
    return updated_library

def search_books(library, query):
    return [book for book in library if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    return total_books, percentage_read

st.title("📚 Personal Library Manager")
library = load_library()

menu = st.sidebar.selectbox("Menu", ["Add Book", "Remove Book", "Search Book", "Display Books", "Statistics"])

if menu == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read")
    if st.button("Add Book"):
        add_book(library, title, author, year, genre, read_status)
        st.success("Book added successfully!")

elif menu == "Remove Book":
    st.subheader("Remove a Book")
    title = st.text_input("Enter book title to remove")
    if st.button("Remove"):
        library = remove_book(library, title)
        st.success("Book removed successfully!")

elif menu == "Search Book":
    st.subheader("Search for a Book")
    query = st.text_input("Enter title or author")
    if st.button("Search"):
        results = search_books(library, query)
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found!")

elif menu == "Display Books":
    st.subheader("Your Library")
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.info("Your library is empty.")

elif menu == "Statistics":
    st.subheader("Library Statistics")
    total_books, percentage_read = display_statistics(library)
    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {percentage_read:.2f}%")
