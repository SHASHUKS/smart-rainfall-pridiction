from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

EMAIL_ADDRESS = "ksshashwath79@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"

# 📧 EMAIL FUNCTION
def send_email(to_email, rainfall, crop, reason, message):
    try:
        subject = "Smart Agriculture Result"
        body = f"""
Message:
{message}

Rainfall: {rainfall}
Crop: {crop}

Reason:
{reason}
"""
        msg = f"Subject: {subject}\n\n{body}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg)
        server.quit()

        print("Email Sent Successfully")

    except Exception as e:
        print("Email Error:", e)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    soil = request.form['soil']

    # 🌱 LOGIC
    if soil == "Clay":
        crop = "Rice"
        reason = "Rice grows well in clay soil due to high water retention."
    elif soil == "Sandy":
        crop = "Groundnut"
        reason = "Groundnut prefers sandy soil for good drainage."
    else:
        crop = "Wheat"
        reason = "Wheat grows best in loamy soil with moderate conditions."

    rainfall = 180
    level = "Normal"

    return render_template(
        'result.html',
        rainfall=rainfall,
        crop=crop,
        level=level,
        reason=reason
    )


# 📧 SEND EMAIL FROM PAGE 2
@app.route('/send_email', methods=['POST'])
def email_send():
    rainfall = request.form['rainfall']
    crop = request.form['crop']
    reason = request.form['reason']
    email = request.form['email']
    message = request.form['message']

    send_email(email, rainfall, crop, reason, message)

    return "Email Sent Successfully! Go back."


if __name__ == "__main__":
    app.run(debug=True)