#  Adidas Scaper - Adidas Discount Notifier

This project will help track great deals on Adidas and notifies you of discounted products when available based on your preferences. 

Implementation uses Python and web scraping techniques to track the Adidas UK website for discounted products that match your specific criteria (gender, category, size). When matching items are found, the system retrieves product details from the Adidas API and sends an email in formatted HTML format containing all relevant information,such as product images, pricing & discount information including direct purchase links. 

## Features

✅ Fetch Adidas Discounts – Retrieves products on sale using the Adidas API.
✅ Email Notification – Sends a structured email with discounted products.
✅ Customizable Search – Users can choose search preferences based on filters such as gender, category, and size.

## Email Notification:-
<img width="1000" alt="Adidas Discount Notification" src="https://github.com/user-attachments/assets/55070a0a-a5e1-43dc-8daa-a3bed4c422fb" />


## Project Structure
📂 `adidas_discount_notifier`  
├── 📄 `main.py`              *Main script execution*  
├── 📄 `email_notify.py`      *Handles email notifications*  
├── 📄 `html_generator.py`    *Generates HTML email content*  
├── 📄 `api_client.py`        *Adidas API requests and product search*  
├── 📄 `models.py`            *Pydantic models for structured data*  
├── 📄 `requirements.txt`     *Required Python dependencies*  
├── 📄 `.env`                 *Stores email credentials (not committed)*  
└── 📄 `README.md`            *Project documentation*


### Python libraries used in this project:-

  -  curl_cffi – For making HTTP requests to fetch product details.
  -  pydantic – For defining structured models and data validation.
  -  rich – For colorful and formatted console output.
  -  smtplib – For sending emails via SMTP.
  -  email.mime – For constructing HTML and plain text emails.
    


## Prerequisites

-  Python 3.8 or higher
-  An email account for sending notifications (currently configured for iCloud)
-  Required environment variables set up for email authentication

## Installation

1.  Clone this repository:

-  git clone [link text](https://github.com/yourusername/adidas-scraper.git)
-  cd adidas-scraper

2.  Create a virtual environment

-  python -m venv venv
-  source venv/bin/activate  # macOS/Linux
-  venv\Scripts\activate     # Windows

3.  Install dependencies:

-  pip install -r requirements.txt


4. Set up environment variables
Create a .env file in the root directory:

-  SMTP_SERVER=smtp.mail.me.com
-  SMTP_PORT=587
-  EMAIL_SENDER=your_email@example.com
-  EMAIL_PASSWORD=your_app_password

5.  Usage

Run the script to fetch current discounts and receive an email notification:
-  python main.py

6.  Customizing Search Parameters

You can modify the search parameters in the main() function:
For example:
-  gender = "Women"          # Options: Women, Men, Kids, Unisex
-  sorttype = "top-sellers"  # Options: price-low-to-high, top-sellers, newest-to-oldest, price-high-to-low
-  size = 9 # UK shoe size



