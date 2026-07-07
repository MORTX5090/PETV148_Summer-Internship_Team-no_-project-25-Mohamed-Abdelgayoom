from flask import Flask, request, render_template, redirect, url_for, session
from scanner import scan_headers
from hardener import generate_fixes
from database import init_db, insert_scan, get_dashboard_stats

app = Flask(__name__)

# Secret key for encrypting sessions (Crucial for the login system)
app.secret_key = 'super_secret_cyber_key_2026' 

# Admin dashboard password (You can change this)
ADMIN_PASSWORD = 'admin'

# Initialize the database when the server starts
init_db()

@app.route('/', methods=['GET'])
def index():
    """Route to render the main home page with public statistics."""
    stats = get_dashboard_stats()
    return render_template('index.html', stats=stats)

@app.route('/scan', methods=['POST'])
def scan():
    """Route to handle the scanning process."""
    target_url = request.form.get('url')
    
    # Check if the URL parameter is provided
    if not target_url:
        return render_template('index.html', error="URL parameter is missing")
        
    scan_result = scan_headers(target_url)
    missing_headers_list = []

    # Process the missing headers if the scan is successful
    if scan_result.get('success') and 'results' in scan_result:
        for item in scan_result['results']:
            if item.get('status') == 'Missing':
                missing_headers_list.append(item.get('header'))
                
        # Generate security fixes
        fixes = generate_fixes(missing_headers_list)
        scan_result['fixes'] = fixes
        
        # Save the scan result to the database
        insert_scan(scan_result['url'], scan_result['score'], scan_result['grade'])

    return render_template('result.html', **scan_result)    

# --- Login Route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route to handle admin authentication."""
    if request.method == 'POST':
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            # Activate the login session
            session['logged_in'] = True 
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid Access Code!")
    return render_template('login.html')

# --- Logout Route ---
@app.route('/logout')
def logout():
    """Route to handle admin logout."""
    # Terminate the session
    session.pop('logged_in', None) 
    return redirect(url_for('index'))

# --- Protected Dashboard Route ---
@app.route('/dashboard', methods=['GET'])
def dashboard():
    """Route to display the admin dashboard (Protected)."""
    # Security Check: Redirect to login if the user is not authenticated
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    stats = get_dashboard_stats()
    return render_template('dashboard.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)