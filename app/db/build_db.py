import sqlite3
import csv
import uuid
from io import StringIO


# Sample CSV data

def create_and_load_bank_data(db_name='top_rates.db', table_name='banks', csv_file='/Users/raksingh/personal/github/top-rates/app/db/banks.csv'):
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
                uninum TEXT,    -- FDIC unique number for banks
                charter_number TEXT, -- Charter Number for credit unions
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
        
        # # Get headers
        headers = next(csv_reader)

        # Insert data
        insert_sql = f'''INSERT INTO {table_name} 
                        (id, name, old_name, rss_id, uninum, website, zipcode, charter_number)
                        VALUES (?, ?, ?, ?, ?, ?,?,?)'''
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


def create_and_load_bank_products_data(db_name='top_rates.db', table_name='bank_products', csv_file='/Users/raksingh/personal/github/top-rates/app/db/products.csv'):
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
                bank_id TEXT,
                bank_name TEXT NOT NULL,
                bank_website TEXT,
                name TEXT NOT NULL,
                type TEXT,
                description TEXT,
                product_url TEXT,
                apy REAL,
                min_deposit REAL,
                min_balance REAL,
                term_months INTEGER,
                compounding_frequency TEXT,
                interest_payment_frequency TEXT,
                additional_info TEXT,
                start_date TEXT,
                end_date TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_sql)
        
        
        # # Parse CSV data
        csv_file = open(csv_file, 'r', encoding='utf-8')
        csv_reader = csv.reader(csv_file)
        
        # # Get headers
        headers = next(csv_reader)

        # Insert data
        insert_sql = f'''INSERT INTO {table_name} 
                        (id, bank_name, name, apy, compounding_frequency, product_url, additional_info)
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
    create_and_load_bank_products_data()
    print("\n✓ Database created successfully!")
    print("  You can query it using: sqlite3 top_rates.db")
