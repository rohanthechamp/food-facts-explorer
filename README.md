# 🥗 Food Facts Explorer

A Flask-based web application that allows users to search for food products and view detailed nutritional information using the OpenFoodFacts API.

---

## 🚀 Features

- 🔍 Search for food products (e.g., snacks, beverages, cereals)
- 📊 View nutritional information:
  - Energy, fats, carbohydrates, proteins, sugars, salt
- 🧾 Ingredient breakdown
- 🟢 Health indicators:
  - Nutri-Score, Eco-Score, Nova Group
- 🖼️ Product image display

---

## 🛠️ Tech Stack

- Flask  
- HTML, CSS, Bootstrap  
- OpenFoodFacts API  
- Jinja2  

---

## ⚙️ How It Works

1. User enters a product name  
2. Flask sends request to OpenFoodFacts API  
3. Response is processed  
4. Data is displayed on UI  

---

## 📸 Screenshots

<!-- Add screenshots here -->
<!-- ![Home](screenshots/home.png) -->
<!-- ![Product](screenshots/product.png) -->

---

## ⚙️ Setup

```bash
git clone https://github.com/rohanthechamp/food-facts-explorer.git
cd food-facts-explorer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python server.py
⚠️ Limitations
Depends on external API
Data may be incomplete
API downtime possible (e.g., 503 errors)
🚀 Future Improvements
Add retry & error handling
Implement caching
Improve UI/UX
Add product comparison
Add filtering options
Deploy the application
📌 Note

This project focuses on practicing API integration and building a dynamic Flask application.

📄 License

Open-source and available under the MIT License.
