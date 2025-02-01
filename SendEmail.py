import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

email = "your_email@gmail.com"
password = "your_password"
server.login(email, password)

server.sendmail(email, "receiver@example.com", "Subject: Test Email\n\nHello, this is a test email.")
server.quit()
