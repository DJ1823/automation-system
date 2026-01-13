Gmail to Google Sheets Automation

🔹 Project Overview

This project is a Python-based automation system that reads unread emails from a Gmail account and stores important email details into a Google Sheet automatically. It uses Google OAuth 2.0 for secure authentication and avoids duplicate entries by tracking previously processed emails.


🔹 Objective

To automate the process of collecting email data and maintaining it in a structured format (Google Sheets) without manual effort.


🔹 Technologies Used

Python
Gmail API
Google Sheets API
OAuth 2.0
Google Cloud Platform


🔹 How the Project Works

The Python script is executed.
Google OAuth authentication is triggered (only the first time).
The script accesses the Gmail inbox and fetches unread emails.
Important email details are extracted:
Sender
Subject
Date
Email body

Extracted data is appended as a new row in Google Sheets.
Processed emails are marked as read.
The last processed email ID is stored to prevent duplicate entries.


🔹 Duplicate Handling
A file named state.json stores the ID of the last processed email.
On every run, previously processed emails are skipped
This ensures no duplicate rows are added to the Google Sheet.


🔹 Authentication & Security
OAuth 2.0 is used instead of passwords.
Access tokens are stored in token.json.
User data remains secure and private.


🔹 APIs Used
Gmail API – to read and modify emails.
Google Sheets API – to write data into Google Sheets.


🔹 Project Structure
Gmail-to-sheets/
│
├── src/
│   ├── main.py
│   ├── gmail_service.py
│   ├── sheets_service.py
│   ├── email_parser.py
│   └── config.py
│
├── proof/
├── requirements.txt
├── README.md
└── .gitignore


🔹 How to Run the Project
pip install -r requirements.txt
python src/main.py


🔹 Use Cases
Customer support email tracking
Internship or job application monitoring
Business enquiry management
Automated email reporting


🔹 Limitations
Only unread emails are processed.
Script execution is manual.
Email order depends on Gmail message order.


🔹 Conclusion
This project successfully automates email data extraction and storage using Google APIs. It reduces manual effort, avoids duplication, and demonstrates practical usage of OAuth authentication and API integration.

