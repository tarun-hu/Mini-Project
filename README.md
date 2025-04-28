# Smart UPI QR Code Payment System

A simple web application that allows businesses and individuals to generate UPI QR codes with a fixed amount for easy digital payments. It also maintains a transaction history and calculates total income.

---

## Features

- UPI QR Code generation with fixed amount.
- Transaction history tracking.
- Total income calculation and display.
- Responsive and clean user interface.
- Dark mode support.
- Lightweight and easy to deploy.

---

## Tech Stack

- **Frontend**:  
  - HTML5  
  - TailwindCSS
- **Backend**:  
  - Python 3  
  - Flask
- **Libraries Used**:  
  - `qrcode` (for QR code generation)  
  - `base64` (for embedding QR codes into HTML)

---


## Project Structure

```
upi-qr-generator/
│
├── static/
│   └── styles.css         # Custom styling
│
├── templates/
│   └── index.html         # Main frontend page
│
├── app.py                 # Flask backend
├── README.md              # Project README
└── requirements.txt       # Python dependencies
```

---

## How It Works

- User fills in:
  - Name
  - UPI ID
  - Amount
- App generates a UPI payment link.
- Link is converted into a scannable QR code.
- Payment details are saved to the transaction history.
- Total income is updated dynamically.

---

## Future Scope

- Database integration (for permanent data storage).
- User login and authentication.
- Export transaction reports.
- Analytics dashboard for earnings visualization.

---

## License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## Contact

For any inquiries or suggestions:  
- **Tarun** - [tarunnokwal1@gmail.com]

---

# Thank you for using Smart UPI QR Code Payment System!
