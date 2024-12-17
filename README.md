# Birthday-Wisher-Automation

## Project Description
This project is a simple Python script that automatically sends personalized birthday wishes via email to individuals whose birthdays match the current date. The script reads data from a CSV file containing recipient details (name, email, date, and month of birth), customizes a letter template, and sends the message using an SMTP email service like Gmail.

## Features

- Reads recipient data (name, email, birthday) from a CSV file.
- Checks if today's date matches any birthday in the CSV.
- Customizes a pre-written letter template with the recipient's name.
- Sends automated emails using Gmail's SMTP server.
- Outputs confirmation logs when emails are successfully sent.

## Prerequisites
### Make sure you have the following:
  - Python 3.x installed.
    #### - Required Python libraries:
        pandas    
        smtplib      
        datetime

       - A Gmail account with App Password enabled.

## Project Files
   - data.csv
   ## The CSV file containing recipient details:
      name,email,date,month
      david,example1@gmail.com,16,6
      john,example2@gmail.com,17,6

   - name: Recipient's name.

   - email: Recipient's email address.

   - date: Birthday date (e.g., 16).

   - month: Birthday month (e.g., 6 for June).

## letter.txt

The letter template:

    Dear [name],
    
    Wishing you a very Happy Birthday! 🎉🎂
    
    Have a wonderful day and an amazing year ahead!
    
    Best regards,
    Your Name

[name] will be replaced with the recipient's actual name.

## Troubleshooting

 - ModuleNotFoundError: Install missing libraries using pip install.

 - SMTP Errors: Make sure your Gmail account has App Passwords enabled and "Allow less secure apps" turned off.

 - Incorrect Data: Check that data.csv is correctly formatted with proper column names.
