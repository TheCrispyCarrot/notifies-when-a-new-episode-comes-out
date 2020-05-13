import smtplib
def SendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    email = 'enter your email here!'
    password = 'enter your password here!'

    #logs into the email with the randomly genorated app password.
    server.login(email, password)

    subject = 'This is an email sent with pyton!'
    body = 'Here is some text that will be put in the body of the email. It is pretty cool!'

    #creating the message by putting the two above varriables togehter.
    message = f"Subject: {subject}\n\n{body}"

    #command that actually sends the emaail
    #the email is sent from your adress to your address
    server.sendmail(email, email, message)

    print("Ayo, the email has been sent!")

SendEmail()
