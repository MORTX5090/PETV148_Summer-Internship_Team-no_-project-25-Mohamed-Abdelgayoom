# Hi i'am MOHAMED ABDUALRAHMAN this my branch (do'nt EDIT OR CHANGE ANYTHING) here

import sqlite3

# Database filename (will be created automatically)
DB_NAME = 'security_scanner.db'

def init_db():
    """Initialize the SQLite database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create the scans table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            score INTEGER NOT NULL,
            grade TEXT NOT NULL,
            scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_scan(url, score, grade):
    """Insert a new scan result into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO scans (url, score, grade)
        VALUES (?, ?, ?)
    ''', (url, score, grade))
    
    conn.commit()
    conn.close()

def get_dashboard_stats():
    """Fetch structured data for the dashboard statistics."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    stats = {}
    
    # 1. Grand Totals (Count of scans per grade)
    cursor.execute('''
        SELECT grade, COUNT(*) as count 
        FROM scans 
        GROUP BY grade 
        ORDER BY grade ASC
    ''')
    stats['totals'] = cursor.fetchall()
    
    # 2. Recent Scans (Latest 10 scans)
    cursor.execute('SELECT url, grade FROM scans ORDER BY scan_date DESC LIMIT 10')
    stats['recent'] = cursor.fetchall()
    
    # 3. Hall of Fame (Grades A+ or A, Grouped by URL to prevent duplicates)
    cursor.execute('''
        SELECT url, grade 
        FROM scans 
        WHERE grade IN ('A+', 'A') 
        GROUP BY url
        ORDER BY MAX(scan_date) DESC LIMIT 10
    ''')
    stats['hall_of_fame'] = cursor.fetchall()
    
    # 4. Hall of Shame (Grade F, Grouped by URL to prevent duplicates)
    cursor.execute('''
        SELECT url, grade 
        FROM scans 
        WHERE grade = 'F' 
        GROUP BY url
        ORDER BY MAX(scan_date) DESC LIMIT 10
    ''')
    stats['hall_of_shame'] = cursor.fetchall()
    
    # 5. Admin History (Full scan history for the administrator)
    cursor.execute('SELECT * FROM scans ORDER BY scan_date DESC')
    stats['admin_history'] = cursor.fetchall()
    
    conn.close()
    return stats