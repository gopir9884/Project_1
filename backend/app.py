from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

FILENAME = "contacts.csv"

# Initialize CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "email"])

# Helper function: Read all contacts
def read_all_contacts():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Helper function: Contact exists?
def contact_exists(name):
    for row in read_all_contacts():
        if row["name"].lower() == name.lower():
            return True
    return False

# Route: Add Contact
@app.route("/api/contacts", methods=["POST"])
def add_contact():
    data = request.json
    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    email = data.get("email", "").strip()

    if not name or not phone or not email:
        return jsonify({"error": "All fields are required"}), 400

    if contact_exists(name):
        return jsonify({"error": "Contact already exists"}), 409

    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    return jsonify({"message": "Contact added successfully"}), 201

# Route: Get all contacts
@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    contacts = read_all_contacts()
    if not contacts:
        return jsonify([]), 200
    return jsonify(contacts), 200

# Route: Search contacts
@app.route("/api/contacts/search", methods=["GET"])
def search_contact():
    term = request.args.get("q", "").lower()
    contacts = read_all_contacts()
    results = [c for c in contacts if term in c["name"].lower()]
    return jsonify(results), 200

# Route: Delete contact
@app.route("/api/contacts/<name>", methods=["DELETE"])
def delete_contact(name):
    contacts = read_all_contacts()
    updated = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(updated) == len(contacts):
        return jsonify({"error": "Contact not found"}), 404

    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(updated)

    return jsonify({"message": "Contact deleted"}), 200

# Route: Update contact
@app.route("/api/contacts/<name>", methods=["PUT"])
def update_contact(name):
    data = request.json
    new_phone = data.get("phone", "").strip()
    new_email = data.get("email", "").strip()

    contacts = read_all_contacts()
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = new_phone
            contact["email"] = new_email
            found = True
            break

    if not found:
        return jsonify({"error": "Contact not found"}), 404

    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(contacts)

    return jsonify({"message": "Contact updated"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
