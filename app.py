from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# =============================
# الصفحة الرئيسية
# =============================
@app.route("/")
def index():
    # ترجع ملف index.html من نفس المجلد
    return send_from_directory('.', 'index.html')

# =============================
# 1) قراءة الباركود (تمثيلية)
# =============================
@app.route("/scan", methods=["POST"])
def scan_qr():
    data = {
        "owner": "عبدالله بن محمد",
        "plate": "أ ب ج 1234",
        "car_model": "Toyota Camry 2020",
        "vin": "1234567890ABCDEFG"
    }
    return jsonify({"status": "success", "car_data": data})

# =============================
# 2) كشف الضرر بالذكاء الاصطناعي (محاكاة)
# =============================
@app.route("/analyze", methods=["POST"])
def analyze_damage():
    severity = random.choice(["Low", "Medium", "High"])
    area = random.choice(["Front-Left", "Front-Right", "Rear-Left", "Rear-Right"])
    return jsonify({
        "status": "success",
        "damage_detected": True,
        "severity": severity,
        "area": area
    })

# =============================
# 3) توليد تقرير LLM
# =============================
@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.json
    report = f"""
تقرير حادث آلي:

المالك: {data['owner']}
المركبة: {data['car_model']}
رقم اللوحة: {data['plate']}

تفاصيل الحادث:
- الموقع: {data['location']}
- الضرر المكتشف: {data['severity']}
- الجهة المتضررة: {data['area']}

يرجى إرسال فرق الدعم المناسبة.
"""
    return jsonify({"status": "success", "report": report})

# =============================
# 4) إرسال البلاغ (محاكاة)
# =============================
@app.route("/send", methods=["POST"])
def send_report():
    return jsonify({"status": "sent_to_najm_and_ems"})

# =============================
# تشغيل السيرفر
# =============================
if __name__ == "__main__":
    app.run(debug=True)


    