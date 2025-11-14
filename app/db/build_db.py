import sqlite3
import csv
import uuid
from io import StringIO


# Sample CSV data

def create_and_load_bank_data(db_name='top_rates.db', table_name='banks', csv_file='institutions.csv'):
    """
    Create a SQLite database and load bank data from CSV.
    
    Parameters:
    - db_name: name of the SQLite database file (default: 'banks.db')
    - table_name: name of the table to create (default: 'banks')
    """
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:      
        # Create table with appropriate columns
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                old_name TEXT,
                rss_id TEXT,
                uninum TEXT,
                type TEXT  NULL,
                routing_number TEXT,
                website TEXT,
                zipcode TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_sql)
        
        # Parse CSV data
        csv_file = open(csv_file, 'r', encoding='utf-8')
        csv_reader = csv.reader(csv_file)
        
        # Get headers
        headers = next(csv_reader)

        # Insert data
        insert_sql = f'''INSERT INTO {table_name} 
                        (id, name, old_name, rss_id, uninum, website, zipcode)
                        VALUES (?, ?, ?, ?, ?, ?,?)'''
        rows_inserted = 0
        
        for row in csv_reader:
            # Generate a unique bank_id
            row.insert(0, str(uuid.uuid4()))
            print(f'Inserting row: {row}')
            cursor.execute(insert_sql, row)
            rows_inserted += 1
            conn.commit()
        print(f'Inserted {rows_inserted} rows into {table_name} table.')
    finally:
        conn.close()


if __name__ == "__main__":
    create_and_load_bank_data()
    print("\n✓ Database created successfully!")
    print("  You can query it using: sqlite3 top_rates.db")
