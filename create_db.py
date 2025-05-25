import sqlite3

# Connect to the SQLite database (or create it)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sample_data = [
    ("Laptop", 2, 750.00),
    ("Headphones", 5, 50.00),
    ("Mouse", 10, 20.00),
    ("Monitor", 3, 200.00),
    ("Keyboard", 4, 30.00)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("Database and table created successfully with sample data.")
