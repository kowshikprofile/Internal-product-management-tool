
# 🛒 Internal Product Management Tool for eCommerce

## 📖 Project Overview
This project is an **internal tool** to manage the product catalog of an eCommerce platform.  
It allows merchandisers and category managers to:

- Define **new product categories** (e.g., Shoes, Smartphones, Shirts)
- Define **custom attributes** for each category (e.g., RAM, OS for smartphones; Size for shoes)
- Create and manage **products** with category-specific attributes
- Ensure scalability for future product categories

---

## ⚙️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS (basic UI)
- **Database:** MySQL (can also use SQLite for testing)
- **IDE:** Visual Studio Code

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone <https://github.com/kowshikprofile/Internal-product-management-tool>
   cd <ecommerce_tool>

2. python -m venv venv
3. python venv\Scripts\activate
4. pip install django
5. python manage.py runserver
6. open http://127.0.0.1:8000/products/
7. open http://127.0.0.1:8000/admin/catalog/