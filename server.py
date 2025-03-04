from flask import Flask, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__, static_folder="static")

CORS(app)  # Enable CORS for frontend requests

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["market_listings"]
collection = db["garbage"]

@app.route("/api/market", methods=["GET"])

def home():
    return render_template("index.html")  # Serve your HTML page

def get_market():
    """Fetch all market listings from MongoDB."""
    items = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB’s internal _id field
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)