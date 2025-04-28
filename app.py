from flask import Flask, render_template, request, jsonify
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

# Global variables to store total income and transaction history
total_income = 0
transactions = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global total_income, transactions
    qr_code = None
    app_name = None
    amount = "0.00"  # Default amount

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        upi_id = request.form.get('upi_id', '').strip()
        amount = request.form.get('amount', '0.00').strip()
        payment_app = request.form.get('payment_app', '')

        # Validate input fields
        if not name or not upi_id:
            return "Error: Name and UPI ID are required", 400

        try:
            amount = float(amount)  # Convert amount to float safely
        except ValueError:
            return "Error: Invalid amount", 400

        # Generate UPI payment URL (Fixed version)
        qr_url = f"upi://pay?pa={upi_id}&pn={name}&tn=Payment&am={amount}&cu=INR"
        print("Generated QR Code URL:", qr_url)  # Debugging log

        # Generate QR Code
        qr_img = qrcode.make(qr_url)
        buffered = BytesIO()
        qr_img.save(buffered, format="PNG")
        qr_code = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Store transaction
        transactions.append({
            'name': name,
            'app': payment_app,
            'amount': amount
        })

        # Update total income
        total_income += amount
        app_name = payment_app

    return render_template('index.html', qr_code=qr_code, app_name=app_name, amount=amount, total_income=total_income, transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
