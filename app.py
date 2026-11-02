from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ከ Frontend ጋር ለማገናኘት

# ለሙከራ የሚሆን የሀሰት ማከማቻ (ከፈለክ ከላይ በሰጠነው የ Supabase ዳታቤዝ ሊንክ ጋር ማገናኘት ትችላለህ)
rooms_db = [
    {"id": 1, "room_number": "101", "room_type": "Single Room", "status": "Available"},
    {"id": 2, "room_number": "202", "room_type": "VIP Suite", "status": "Available"}
]

bookings_db = []
inventory_db = [
    {"id": 1, "item_name": "ጤፍ (Teff)", "quantity": 15, "status": "በቂ አለ"},
    {"id": 2, "item_name": "የምግብ ዘይት (Oil)", "quantity": 4, "status": "ሊያልቅ ነው።"}
]

# 1. ክፍሎችን የማየት እና የማስያዝ API
@app.route('/api/rooms', methods=['GET', 'POST'])
def handle_rooms():
    if request.method == 'POST':
        data = request.json
        guest_name = data.get('guest_name')
        room_type = data.get('room_type')
        
        booking = {"guest_name": guest_name, "room_type": room_type, "status": "የተያዘ"}
        bookings_db.append(booking)
        return jsonify({"message": "ክፍሉ በተሳካ ሁኔታ ተይዟል!", "booking": booking}), 201
    
    return jsonify(rooms_db)

# 2. የስቶር (Inventory) መረጃዎችን ማየት API
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory_db)

# 3. የኩሽና ትዕዛዞችን መቀበያ API
@app.route('/api/kitchen/orders', methods=['GET', 'POST'])
def handle_kitchen_orders():
    if request.method == 'POST':
        order_data = request.json
        return jsonify({"message": "ትዕዛዙ ወደ ኩሽና ተልኳል!", "order": order_data}), 201
    return jsonify({"message": "アクቲቭ ትዕዛዞች የሉም"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ከ Supabase ጋር የሚገናኝበት ኮድ እዚህ ይዘጋጃል
# ለምሳሌ እንግዶች ሲመዘገቡ በቀጥታ ወደ Supabase bookings ሠንጠረዥ እንዲገባ ይደረጋል

@app.route('/api/rooms', methods=['GET', 'POST'])
def handle_rooms():
    if request.method == 'POST':
        data = request.json
        guest_name = data.get('guest_name')
        room_type = data.get('room_type')
        
        # እዚህጋ ከ Supabase ጋር በመገናኘት ዳታው ይጻፋል
        return jsonify({"message": "ክፍሉ በተሳካ ሁኔታ በዳታቤዝ ተመዝግቧል!", "guest": guest_name}), 201

    return jsonify({"message": "የክፍሎች ዝርዝር ከዳታቤዝ"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ከ Frontend ጋር ለማገናኘት

# በ Supabase ውስጥ ካሉን ሠንጠረዦች ጋር የሚመሳሰሉ የቦታ መረጃዎች
rooms_db = [
    {"id": 1, "room_number": "101", "room_type": "Single Room", "status": "Available"},
    {"id": 2, "room_number": "202", "room_type": "VIP Suite", "status": "Available"}
]

bookings_db = []
inventory_db = [
    {"id": 1, "item_name": "ጤፍ (Teff)", "quantity": 15, "status": "በቂ አለ"},
    {"id": 2, "item_name": "የምግብ ዘይት (Oil)", "quantity": 4, "status": "ሊያልቅ ነው።"}
]

# 1. ክፍሎችን የማየት እና የማስያዝ API
@app.route('/api/rooms', methods=['GET', 'POST'])
def handle_rooms():
    if request.method == 'POST':
        data = request.json
        guest_name = data.get('guest_name')
        room_type = data.get('room_type')
        
        booking = {"guest_name": guest_name, "room_type": room_type, "status": "የተያዘ"}
        bookings_db.append(booking)
        print(f"አዲስ እንግዳ ተመዝግቧል: {guest_name} - {room_type}")
        return jsonify({"message": "ክፍሉ በተሳካ ሁኔታ ተይዟል!", "booking": booking}), 201
    
    return jsonify(rooms_db)

# 2. የስቶር (Inventory) መረጃዎችን ማየት API
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory_db)

# 3. የኩሽና ትዕዛዞችን መቀበያ API
@app.route('/api/kitchen/orders', methods=['GET', 'POST'])
def handle_kitchen_orders():
    if request.method == 'POST':
        order_data = request.json
        return jsonify({"message": "ትዕዛዙ ወደ ኩሽና ተልኳል!", "order": order_data}), 201
    return jsonify({"message": "አክቲቭ ትዕዛዞች የሉም"})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)