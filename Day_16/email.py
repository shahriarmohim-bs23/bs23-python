import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = ""
password = ""

receiver = input("Receiver Email")

context = ssl.create_default_context()

