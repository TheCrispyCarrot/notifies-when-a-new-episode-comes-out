import smtplib
import requests
from bs4 import BeautifulSoup
import time

#defining a function to send an email saying there is a new episode out
def SendEmail():
    #uses values for a gmail email. this can be found on line if you have a different email.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #varriables for email and password
    email = 'enter your email here!'
    password = 'enter your password here!'

    #logs into the email with the randomly genorated app password.
    server.login(email, password)

    subject = 'Black Clover Episode Detected With Python!'
    body = 'looks like there is a new episode of black clover to watch! here is the link: https://www.wcoanimesub.tv/anime/black-clover-tv-english-subbed'

    #creating the message by putting the two above varriables togehter.
    message = f"Subject: {subject}\n\n{body}"

    #command that actually sends the emaail
    server.sendmail(email, email, message)

    #print("Ayo, the email has been sent!")



##############################################################################################################################################
#turns the episode list on the website into a list
URL = 'https://www.wcoanimesub.tv/anime/black-clover-tv-english-subbed'
#headers can be found by typing 'What is my user agent' into your browser and copying the result
headers = {"enter your headers here!'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
epasodes = soup.find(id = "sidebar_right3").get_text()
epasodes_list = list(epasodes.split())

#x is the most episode that is about to be released
x = '130'
while 1==1:
    #checks to see if the latest episode is in the list
    #and sends an email if there is one
    if x in epasodes_list:
        SendEmail()
        #converts the x value into an integer in order to add one to it accounting for the next episode
        #and then returns it to its string form in order to search the list for the new value.
        x = int(x)
        x += 1
        x = str(x)
    else:
        #delays the program from running for an hour if a new episode is not detected. 
        time.sleep(3600)

    time.sleep(10)

