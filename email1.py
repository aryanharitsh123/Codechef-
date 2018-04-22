import smtplib

host = "smtp.gmail.com"
port = 587
username = "aryanharitsh@gmail.com"
password = "Password :)"
from_email = username
to_list=["amanharitsh123@gmail.com", "aryanharitsh@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn.quit()
