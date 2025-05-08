# Django Recipe Vault 🍲🔐

A secure and feature-rich recipe management web application built with Django. This project demonstrates authentication-based access control, CRUD operations, image uploads, and real-time recipe search functionality. It’s designed for developers exploring Django's full-stack capabilities with a focus on clean architecture and security.

---

## 🔑 Features

- ✅ User Registration, Login, and Logout  
- ✅ Authenticated recipe management (Add / Update / Delete)  
- ✅ Public recipe viewing  
- ✅ Image upload for each recipe  
- ✅ Search recipes by title or ingredients  
- ✅ Django messages for feedback and alerts  
- ✅ Responsive UI using Bootstrap 

---

## 🛠️ Technologies Used

- Python 3.x  
- Django  
- Postgresql (can switch to Sqllite)  
- HTML, CSS (Bootstrap)  
- Pillow (for image handling)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Fareehagit/django-recipe-vault.git
cd django-recipe-vault

2. Create a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Apply Migrations
bash
python manage.py makemigrations
python manage.py migrate
5. Run the Development Server
bash
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

📂 Folder Structure
django-recipe-vault/
│
├── vege/               # Main app (models, views, urls)
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # Uploaded recipe images
├── manage.py

🙋‍♀️ Author
Fareeha Liaqat
Budding Django Developer passionate about clean web design and back-end logic.
