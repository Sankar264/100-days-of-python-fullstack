import smtplib
import ssl
from email.message import EmailMessage
sender_email="ksankar8096@gmail.com"
password="weiydywidnspgrzg"
receiver_email="rbharatreddy311@gmail.com"
message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail"
message.set_content(f"""
APEXNOVA TECHNOLOGIES

SAMPLE – FICTIONAL DOCUMENT

FICTIONAL

Date:

13 July 2026

Offer Reference:

APX/HR/2026/080

To,

Mr. Arjun Mehta

45 Lakeview Residency

Orion City, India

Subject: Offer of Employment

Dear Mr. Arjun Mehta,

We are pleased to offer you the position of Senior Software Architect with ApexNova Technologies. This is a fictional sample offer letter created for educational and design purposes only.

Your proposed employment details are as follows:

Designation

Senior Software Architect

Location

Orion City Development Center

Joining Date

1 August 2026

Annual CTC

(Fictional)

₹80,00,000

per annum

Compensation Structure (Fictional)

Component

	

Amount (₹)




Basic Salary

	

32,00,000




House Rent Allowance

	

12,80,000




Special Allowance

	

15,20,000




Performance Bonus

	

10,00,000




Retention Bonus

	

5,00,000




Other Benefits

	

5,00,000




Total CTC

	

80,00,000

Terms & Conditions

This document is a fictional sample only and does not represent a real employment offer.

The compensation figures shown above are for demonstration purposes.

No legal rights, obligations, or employment relationship are created by this sample.

This format may be used for portfolio, presentation, or document-design practice.

Kindly sign below as an acknowledgment of receipt of this fictional sample document.

For ApexNova Technologies

_____________________

Priya Raman

Head – Human Resources

Candidate Acknowledgment

_____________________

Arjun Mehta

Date: _______________""")
context=ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
     
