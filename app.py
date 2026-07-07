# Hi i'am MOHAMED ABDELGAYOOM this my branch (do'nt EDIT OR CHANGE ANYTHING) here

from flask import Flask,request,render_template,jsonify
from scanner import scan_headers
from hardener import generate_fixes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_url = request.form.get('url')
    if not target_url:
        return jsonify({"success": False, "error": "URL parameter is missing"})
    scan_result = scan_headers(target_url)
    missing_headers_list =[]

    if scan_result.get('success') and  'results' in scan_result:
        for item in scan_result['results']:
            if item.get('status') == 'Missing':
                missing_headers_list.append(item.get('header'))
        fixes = generate_fixes(missing_headers_list)
        scan_result['fixes'] = fixes
    return jsonify(scan_result)     

if __name__ == '__main__':
    app.run(debug=True)

