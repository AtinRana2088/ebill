from flask import Flask, render_template, request, redirect, session, url_for, flash
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a strong secret key

# Load admin credentials from JSON file
def load_admins():
    with open("admins.json", "r") as file:
        return json.load(file)

# Function to send email
def send_email(buyer_email, subject, body):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Use app password for Gmail

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = buyer_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    server.sendmail(sender_email, buyer_email, message.as_string())
    server.quit()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admins = load_admins()
        
        if username in admins and admins[username] == password:
            session['admin'] = username
            return redirect(url_for('generate_bill'))
        else:
            flash("Invalid credentials. Try again.", "danger")
    
    return render_template('login.html')

@app.route('/generate_bill', methods=['GET', 'POST'])
def generate_bill():
    if 'admin' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        gst = amount * 16 / 100 # Change 16 to your respective GST %
        total_amount = amount + gst
        rounded_total = round(total_amount)
        buyer_email = request.form['buyer_email']
        
        bill_content = f"""
        E-Bill
        ------------------------
        Amount: {amount:.2f}
        GST (16%): {gst:.2f}
        ------------------------
        Total: {total_amount:.2f}
        ------------------------
        Roundoff: {rounded_total}
        """
        
        send_email(buyer_email, "Your E-Bill", bill_content)
        flash("Bill sent successfully!", "success")
    
    return render_template('generate_bill.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
