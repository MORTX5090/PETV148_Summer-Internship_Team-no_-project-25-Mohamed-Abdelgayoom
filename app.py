# Hi i'am MOHAMED ABDELGAYOOM this my branch (do'nt EDIT OR CHANGE ANYTHING) here

from flask import Flask,request,render_template,jsonify
from scanner import scan_headers

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
    return jsonify(scan_result)

if __name__ == '__main__':
    app.run(debug=True)
