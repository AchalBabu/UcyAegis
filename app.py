from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Mail, Message
from ganga import bot_response
import os

app = Flask(__name__)

# =========================
# SECRET KEY
# =========================

app.secret_key = "change-this-secret"

# =========================
# MAIL CONFIGURATION
# =========================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Render Environment Variables
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():
    return render_template('index.html')

# =========================
# CHATBOT API
# =========================

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    user_message = data.get("message")

    response = bot_response(user_message)

    return jsonify({
        "reply": response
    })

# =========================
# PRODUCTS PAGE
# =========================

@app.route('/products')
def products():
    return render_template('products.html')

# =========================
# CONTACT PAGE
# =========================

@app.route('/contact')
def contact():
    return render_template('contact.html')

# =========================
# CONTACT FORM SUBMIT
# =========================

@app.route('/send-message', methods=['POST'])
def send_message():

    try:

        # Form Data
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')

        # Check Environment Variables
        if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
            return "ERROR: MAIL ENV VARIABLES NOT FOUND"

        # Create Email
        msg = Message(
            subject=f"UcyAegis Contact Form | {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']]
        )

        # Email Body
        msg.body = f"""
New Contact Form Submission

==============================

Name: {name}

Email: {email}

Message:
{user_message}

==============================
"""

        # Send Email
        mail.send(msg)

        flash(
            "Thank You For Contacting UcyAegis. We Will Contact You Soon.",
            "success"
        )

    except Exception as e:

        print("MAIL ERROR:", e)

        flash(
            f"Error Sending Message: {e}",
            "danger"
        )

    return redirect(url_for('contact'))

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)
