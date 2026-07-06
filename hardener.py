# Dictionary containing fixing commands for both Nginx and Apache servers
FIX_SNIPPETS = {
    'Content-Security-Policy': {
        'nginx': "add_header Content-Security-Policy \"default-src 'self';\";",
        'apache': "Header always set Content-Security-Policy \"default-src 'self'\""
    },
    'Strict-Transport-Security': {
        'nginx': 'add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;',
        'apache': 'Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"'
    },
    'X-Frame-Options': {
        'nginx': 'add_header X-Frame-Options "SAMEORIGIN" always;',
        'apache': 'Header always set X-Frame-Options "SAMEORIGIN"'
    },
    'X-Content-Type-Options': {
        'nginx': 'add_header X-Content-Type-Options "nosniff" always;',
        'apache': 'Header always set X-Content-Type-Options "nosniff"'
    },
    'Referrer-Policy': {
        'nginx': 'add_header Referrer-Policy "no-referrer-when-downgrade" always;',
        'apache': 'Header always set Referrer-Policy "no-referrer-when-downgrade"'
    },
    'Permissions-Policy': {
        'nginx': 'add_header Permissions-Policy "geolocation=(), microphone=()" always;',
        'apache': 'Header always set Permissions-Policy "geolocation=(), microphone=()"'
    }
}

def generate_fixes(missing_headers):
    """
    Takes a list of missing headers and returns the corresponding 
    configuration snippets for Nginx and Apache servers.
    """
    # Create an empty dictionary to store the output results
    fixes = {
        'nginx': [],
        'apache': []
    }
    
    # Loop through each missing header provided by the scanner
    for header in missing_headers:
        # Check if the missing header exists in our FIX_SNIPPETS dictionary
        if header in FIX_SNIPPETS:
            # Append the Nginx fix code to the nginx list
            fixes['nginx'].append(FIX_SNIPPETS[header]['nginx'])
            # Append the Apache fix code to the apache list
            fixes['apache'].append(FIX_SNIPPETS[header]['apache'])
            
    # Return the final dictionary containing all the fixes
    return fixes
