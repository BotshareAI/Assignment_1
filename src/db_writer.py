# db_writer.py
# This module writes matched test data into a local SQLite database (ideal_function.db)

import sqlite3  # Import built-in SQLite interface
import os       # To handle filesystem paths


def write_to_database(df, db_path="db/ideal_function.db"):
    """
    Writes the matched test data (DataFrame) into a SQLite database table named 'matched_points'.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing columns ['x', 'y', 'delta_y', 'ideal_function']
    - db_path (str): The file path to the SQLite database (default is 'db/ideal_function.db')
    """

    # Ensure that the database folder exists before writing
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to the SQLite database file (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create the table (only if it doesn't already exist)
    # This table stores each test point and its assigned ideal function
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matched_points (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-generated row ID
            x REAL NOT NULL,                       -- X value of the test point
            y REAL NOT NULL,                       -- Y value of the test point
            delta_y REAL NOT NULL,                 -- Absolute deviation from the ideal function
            ideal_function TEXT NOT NULL           -- Name of the ideal function (e.g., 'y12')
        )
    """)

    # Clear old data in case this is a re-run (optional, for reproducibility)
    cursor.execute("DELETE FROM matched_points")

    # Insert each row from the DataFrame into the table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO matched_points (x, y, delta_y, ideal_function)
            VALUES (?, ?, ?, ?)
        """, (row["x"], row["y"], row["delta_y"], row["ideal_function"]))

    # Commit changes to make them persistent
    conn.commit()

    # Close the connection to free up resources
    conn.close()

    # Confirm that data was written successfully
    print(f"Inserted {len(df)} matched test points into the database: {db_path}")
