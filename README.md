# HTTP-Security-Headers-Hardener
A smart web security platform that scans HTTP Security Headers, identifies security misconfigurations, provides a security score, and generates ready-to-use middleware code to implement recommended security headers and strengthen web application protection.

# HTTP Security Headers Hardener

هذا المشروع هو أداة أمنية متكاملة لفحص رؤوس (Headers) الأمان في مواقع الويب، وتقديم توصيات لتحسينها بناءً على معايير OWASP العالمية.

## 🛠 التكنولوجيا المستخدمة
- **Backend:** Python / Flask
- **Frontend:** HTML5 / Bootstrap 5
- **Scanner:** Python Requests Library
- **Database:** SQLite
- **Security Standards:** OWASP & Mozilla Observatory

## 👥 فريق العمل وتوزيع المهام
تم تقسيم العمل إلى فروع (Branches) لضمان تنظيم الكود:

| المهمة | الفرع (Branch) | المسؤوليات |
| :--- | :--- | :--- |
| **Frontend** | `frontend` | تصميم الواجهات وصفحة النتائج باستخدام Bootstrap. |
| **Scanner** | `scanner` | تطوير محرك الفحص ومقارنة النتائج بمعايير OWASP. |
| **Database** | `database` | بناء جداول البيانات وإدارة سجل الفحوصات (History). |
| **Team Leader** | `main` | الربط بين جميع الأجزاء (Flask)، الاختبار النهائي، والرفع. |

## 🚀 كيف تبدأ العمل؟
1. **قبول الدعوة:** تأكد من قبول دعوة الـ Collaboration على GitHub.
2. **سحب المشروع:**
   ```bash
   git clone [https://github.com/MORTX5090/HTTP-Security-Headers-Hardener.git](https://github.com/MORTX5090/HTTP-Security-Headers-Hardener.git)