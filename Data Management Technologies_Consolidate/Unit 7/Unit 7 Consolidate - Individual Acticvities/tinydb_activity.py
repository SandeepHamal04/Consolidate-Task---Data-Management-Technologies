# Import TinyDB and Query
from tinydb import TinyDB, Query

# Create or open a TinyDB database file called books_db.json
db = TinyDB("books_db.json")

# Clear the database so the script can be run again without duplicating records
db.truncate()

# Insert sample records into the database
db.insert({
    "title": "Database Basics",
    "author": "Sandeep Hamal",
    "year": 2021,
    "category": "Databases"
})

db.insert({
    "title": "Web Design Guide",
    "author": "Subham Chaudhary",
    "year": 2020,
    "category": "Web Design"
})

db.insert({
    "title": "Python Made Easy",
    "author": "Prakash Sapp",
    "year": 2022,
    "category": "Programming"
})

# Insert a new record
db.insert({
    "title": "Cyber Security Essentials",
    "author": "Majid Anwar",
    "year": 2023,
    "category": "Cyber Security"
})

# Create a query object
Book = Query()

# Retrieve all records where the category matches "Programming"
programming_books = db.search(Book.category == "Programming")

print("Programming Books:")
print(programming_books)

# Update an existing record
db.update({"year": 2024}, Book.title == "Python Made Easy")

# Retrieve all records after the update
all_books = db.all()

print("All Books After Update:")
print(all_books)