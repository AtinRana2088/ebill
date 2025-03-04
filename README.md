# E-Bill Generator Web App

This is a simple web application for generating and sending e-bills. Admins can log in, generate bills, calculate GST, and send the bills via email.

## Features
- **Admin Login:** Secure login with credentials stored in `admins.json`.
- **Bill Generation:** Enter an amount, calculate GST (16%), and round off the total.
- **Email Sending:** Send bills via email using SMTP.
- **Flash Messages:** Inform users about successful actions and errors.

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/AtinRana2088/ebill.git
   cd ebill
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```sh
   python app.py
   ```
> **For App Password**, read: [How to generate an app password?](https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en) or directly create: [an app pasword here](https://myaccount.google.com/apppasswords)


## Admin Credentials Format (`admins.json`)
```json
{
  "admin1": "password123",
  "admin2": "securepass456"
}
```

## Project Structure
```
📂 ebill
│── LICENSE
│── app.py             # Flask Application
│── admins.json        # Admin Login Credentials
│── requirements.txt   # Dependencies
│── templates/
│   │── login.html         # Admin Login Page
│   │── generate_bill.html # Bill Generation Page
└── README.md          # Documentation
```

## License
This project is licensed under the **MIT License**.

---
🚀 **Now your ebill system is ready to use!**
