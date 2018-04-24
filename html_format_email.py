from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "aryanharitsh@gmail.com"
password = "Password"
from_email = username
to_list = ["aryanharitsh@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)


the_msg = MIMEMultipart("Alternative")
the_msg['Subject'] = "Hello There"
the_msg['From'] = username
#the_msg['To'] = to_list
plain_text = "Testing the message"

html_text = """\
<html>
 <head></head>
 <body>
  <p>Hey!</br>
   Testing the email <b>message</b>. Made By <a href = 'http://joincfe.com'>Team CFE</a>
  </p>
 </body>
</html>
"""

part_1 = MIMEText(plain_text, 'plain')
part_2 = MIMEText(html_text,"html")
the_msg.attach(part_1)
the_msg.attach(part_2)
#print(the_msg.as_string())
email_conn.sendmail(from_email, to_list, the_msg.as_string())
email_conn.quit()
