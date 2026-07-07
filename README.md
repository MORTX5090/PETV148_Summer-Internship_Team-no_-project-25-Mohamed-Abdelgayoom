# PETV148_Summer Internship: HTTP Security Headers Hardener

<div align="center">

  <h3>Automated Security Web Application</h3>

  <p>
    An intelligent security tool designed to analyze HTTP security headers, assess vulnerabilities, and provide actionable hardening configurations for web servers.
  </p>

  <br />

  <a href="https://secureheader-pro.onrender.com"><View The Webside Now !</strong></a>
  
</div>

---

## 📋 Project Overview
This project is an automated security scanner and hardener developed for the **PETV148 Summer Internship**. It identifies security misconfigurations (such as missing CSP, X-Frame-Options, or HSTS headers) and provides immediate, server-ready hardening code for Apache and Nginx environments to mitigate common vulnerabilities like XSS and Clickjacking.

## 🚀 Key Features
*   **Intelligent Scanning:** Real-time analysis of target URLs for security header compliance.
*   **Automated Hardening:** Generates configuration snippets to instantly secure web servers.
*   **Admin Dashboard:** Secure interface for scanning history and system statistics.
*   **Responsive UI:** Built with modern CSS (Glassmorphism design) for a professional user experience.

## 🛠️ Technical Stack
*   **Backend:** Flask (Python)
*   **Frontend:** Bootstrap 5, Custom CSS
*   **Database:** SQLite
*   **Deployment:** Render Cloud Platform

## ⚙️ How to Run Locally
Ensure you have Python installed, then follow these steps:

```bash
# 1. Clone the repository
git clone [https://github.com/MORTX5090/PETV148_Summer-Internship_Team-no_-project-25-Mohamed-Abdelgayoom.git](https://github.com/MORTX5090/PETV148_Summer-Internship_Team-no_-project-25-Mohamed-Abdelgayoom.git)

# 2. Navigate to the project directory
cd PETV148_Summer-Internship_Team-no_-project-25-Mohamed-Abdelgayoom

# 3. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
