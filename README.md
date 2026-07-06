# HTTP-Security-Headers-Hardener
A smart web security platform that scans HTTP Security Headers, identifies security misconfigurations, provides a security score, and generates ready-to-use middleware code to implement recommended security headers and strengthen web application protection.

# HTTP Security Headers Hardener

This project is a comprehensive security tool for scanning website Security Headers and providing recommendations to improve them based on global OWASP standards.

## 🛠 Technologies Used
- **Backend:** Python / Flask
- **Frontend:** HTML5 / Bootstrap 5
- **Scanner:** Python Requests Library
- **Database:** SQLite
- **Security Standards:** OWASP & Mozilla Observatory

## 📂 Project Architecture

This overview explains the contents of each file and its role in the system:

| File/Folder | Primary Function | Technologies Used |
| :--- | :--- | :--- |
| `app.py` | Main file (Controller) to link interfaces and engines | Flask |
| `scanner.py` | Website scanning engine to fetch and analyze Security Headers | Python Requests |
| `database.py` | Database connection management and saving scan records | SQLite |
| `templates/` | User interfaces folder (HTML files) | Jinja2 |
| `static/` | Design files (CSS) and media (Assets) | Bootstrap, CSS |
| `requirements.txt` | List of libraries and software requirements for the project | pip |

---

## 👥 Team & Task Distribution
The work has been divided into Branches to ensure code organization:

| Task | Branch | Responsibilities |
| :--- | :--- | :--- |
| **Frontend** | `frontend` | Designing interfaces and the results page using Bootstrap. |
| **Scanner** | `scanner` | Developing the scanning engine and comparing results with OWASP standards. |
| **Database** | `database` | Building database tables and managing the scan history. |
| **Team Leader** | `main` | Linking all parts together (Flask), final testing, and deployment. |

## 🚀 How to Get Started?
1. **Accept the Invitation:** Ensure you accept the Collaboration invitation on GitHub.
2. **Clone the Project:**
   ```bash
   git clone [https://github.com/MORTX5090/HTTP-Security-Headers-Hardener.git](https://github.com/MORTX5090/HTTP-Security-Headers-Hardener.git)