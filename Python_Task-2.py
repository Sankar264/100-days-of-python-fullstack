import segno

# Developer Profile Details
profile = """
================================
        DEVELOPER PROFILE
================================

Name: Kontyana Sai Sankar Rao

Role: Python & React Developer

Skills:
Python
SQL
HTML
CSS
JavaScript
React

Email:
ksankar8096@gmail.com

LinkedIn:
https://www.linkedin.com/in/sai-sankar-rao-kontyana-3318a4318/

GitHub:
https://github.com/Sankar264

YouTube:
https://www.youtube.com/

================================
        THANK YOU!
================================
"""

# Create QR Code
qr = segno.make(profile)

# Save QR Code
qr.save("developer_profile.png", scale=10)

print("Developer Profile QR Code Created Successfully!")
