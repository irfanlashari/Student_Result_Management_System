import sqlite3

def create_db():
    try:
        # Use context manager to ensure the connection is closed after use
        with sqlite3.connect('rms.db') as con:
            cur = con.cursor()

            # Set journal mode to WAL (Write-Ahead Logging) to reduce locking issues
            cur.execute("PRAGMA journal_mode=WAL;")
            con.commit()

            # Create tables if not exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS course (
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    duration TEXT,
                    charges TEXT,
                    description TEXT
                )
            """)
            con.commit()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    roll INTEGER TEXT,
                    name TEXT,
                    email TEXT,
                    gender TEXT,
                    dob TEXT,
                    contact INTEGER,
                    admission INTEGER,
                    course INTEGER,
                    state TEXT,
                    city TEXT,
                    pin INTEGER,
                    address TEXT,
                    FOREIGN KEY (course) REFERENCES course(cid)
                )
            """)
            con.commit()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS result (
                    rid INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll INTEGER,
                    name TEXT,
                    course TEXT,
                    marks_ob TEXT,
                    full_marks TEXT,
                    per TEXT,
                    FOREIGN KEY (roll) REFERENCES student(roll)
                )
            """)
            con.commit()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    eid INTEGER PRIMARY KEY AUTOINCREMENT,
                    f_name TEXT,
                    l_name TEXT,
                    contact TEXT,
                    email TEXT,
                    question TEXT,
                    answer TEXT,
                    password TEXT
                )
            """)
            con.commit()

            print("Database and tables created successfully.")

    except sqlite3.DatabaseError as e:
        print(f"Error creating database: {str(e)}")

# Run the function to create the database
create_db()
