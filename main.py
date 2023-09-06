import schedule, time, os, smtplib,random
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText

password = os.environ["mailPassword"]
username = os.environ["username"]
def sendMail(email):
  email = email
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = "ilya.mikhalchyk.kananenka@gmail.com" 
  msg['From'] = username 
  msg['Subject'] = "Take a BREAK" 
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 

f =open(".tutorial/quotes.txt","r")
for line in f:
  QuotesBook =line.split("',")
n = random.randint(0,163)
QuoteOftheDay = QuotesBook[n]

f.close()

def wring():
  print("⏰")
  sendMail(QuoteOftheDay)

schedule.every(10).days.do(wring)#replace with days

while True:
  schedule.run_pending()
  time.sleep(5)