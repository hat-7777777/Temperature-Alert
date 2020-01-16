import random, time, smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global email
global password
global send_to_email

email = "pythonmailtest7777777"
password = "123!@#qwe"

send_to_email = input("What email should receive temperature reports? ")

def main():
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = "Temperature Report"
    
    temperature = round(random.uniform(40.0, 80.0), 1)
    time = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    msg.attach(MIMEText(f"The temperature is {temperature}°C at {time}.", "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    print(f"Sent email at {time}")
    msg = None
    server.quit()

while True:
    main()
    time.sleep(60)
