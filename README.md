# 📦 Packaging Box Calculator (Django + OpenCV)

A modern **dark‑themed web app** built with Django and OpenCV that allows users to upload product images, automatically detect dimensions, and calculate packaging box size and estimated cost.  
The UI is styled with **Bootstrap 5**, **Bootstrap Icons**, and custom CSS for a sleek dashboard experience.

---

## ✨ Features
- 🖤 **Dark Theme UI** with sidebar navigation
- 📂 **Image Upload** (drag & drop or browse)
- 🔍 **Automatic Dimension Detection** using OpenCV
- 📦 **Box Size Calculation** with padding
- 💰 **Cost Estimation** based on volume
- 🖼️ **Results Card** showing product image and details
- 📑 **Sidebar Navigation** with clickable options (Dashboard, Upload, Results, Settings)

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x
- **Frontend:** Bootstrap 5, Bootstrap Icons, Custom CSS
- **Image Processing:** OpenCV
- **Database:** SQLite (default, can be swapped)

---

## ⚙️ Installation

1.cd packaging-app
Create virtual environment

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies

bash
pip install -r requirements.txt
Example requirements.txt:

Code
Django>=5.0
opencv-python
Run migrations

bash
python manage.py migrate
Start development server

bash
python manage.py runserver
Open in browser:
👉 http://127.0.0.1:8000


Dashboard: Sidebar + Navbar in dark theme

Upload Form: Drag & drop styled box

Results Card: Product image + dimensions + cost

🚀 Future Improvements
Collapsible sidebar for mobile

Loading spinner during calculation

User authentication for saved results

Export results as PDF

👩‍💻 Author
Built by Megha using Django + OpenCV.


