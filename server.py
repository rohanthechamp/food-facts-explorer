from flask import Flask, render_template, request, flash
import secrets
from flask_bootstrap import Bootstrap
import openfoodfacts
from pprint import pprint
import json
from json import JSONDecodeError
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] =  os.environ.get('SECRET_KEY')
app.config["WTF_CSRF_ENABLED"] = True

Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home_function():
    return render_template("index.html")


def fetch_data(user_query):
    if not user_query:
        raise ValueError("Search query cannot be empty")

    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")

    try:
        # Search for product
        response = api.product.text_search(query=user_query, page=1, page_size=1)

        if not response or not response.get("products"):
            raise ValueError("No products found for this search")

        product_code = response["products"][0]["code"]
        print("Code found:", product_code)

        #  product details
        response1 = api.product.get(product_code)

        if not response1:
            raise ValueError("Could not fetch product details")

        # Process categories
        categories = response1.get("categories", "")
        category = (
            categories.split(",")[1].strip()
            if categories and len(categories.split(",")) > 1
            else categories
        )

        product_details = {
            "Product name": response1.get("product_name", "Name not available"),
            "Categories": category or "Category not available",
            "Images_url": {
                "thumbnail_url": response1.get("image_ingredients_url")
                or "/static/placeholder.jpg",
                "image_url": response1.get("image_url") or "/static/placeholder.jpg",
            },
            "Nutritional_Info": response1.get("nutriments") or {},
            "Nutri_Score": response1.get("nutriscore_grade", "Not available"),
            "Nova_Group": response1.get("nova_group", "Not available"),
            "Eco_Score": response1.get("ecoscore_grade", "Not available"),
            "Labels_Certifications": response1.get("labels", "No certifications"),
            "Ingredients": response1.get(
                "ingredients_text", "Ingredients not available"
            ),
        }

        print(f"Generated product details. Verifying length: {len(product_details)}")
        return product_details

    except ValueError as ve:
        print(f"Validation Error: {str(ve)}")
        raise
    except Exception as e:
        if e.data.status == 503:
            raise ValueError("Server Error: Service Temporarily Unavailable")

        
        print(f"Error Occurred: {str(e)}",e)
        raise ValueError("An error occurred while fetching product data")


@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    try:

        if request.method == "POST":
            user_query = request.form.get("query")
        else:
            user_query = request.args.get("query")

        if not user_query:
            flash("Please provide a search query", "error")
            return render_template("index.html")

        product_details = fetch_data(user_query)
        return render_template("product.html", product_details=[product_details])
    except ValueError as ve:
        flash(str(ve), "error")
        return render_template("index.html")
    except Exception as e:
        flash("An unexpected error occurred", "error")
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
