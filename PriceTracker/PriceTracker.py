import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/Coup-Card-Game-Resistance-Universe/dp/B00GDI4HX4/ref=sr_1_3?dchild=1&keywords=coup&qid=1596555211&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    titleinfo = soup.find(id="productTitle").getText() # uses the id to find the content from the URL

    title = (titleinfo.strip()) # .strip removes the extra spaces

    print(title)

    priceString = soup.find(id="priceblock_ourprice").getText()

    price = float(priceString[5:]) # removes the 'CND$' from the text and converts the number string into a float 

    print(price)

    if (price < 23):
        send_mail(title, URL)

def send_mail(name, link): # using smtplib to send mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # makes a connection between emails
    server.starttls()
    server.ehlo()

    server.login('rishivaya2@gmail.com', 'zmgsqpvamfighpxa') # app password from google app passwords

    subject = 'Price fell down for', name
    body = "check amazon link", link

    msg = f"Subject: {subject}\n\n{body}" # 'f' as a prefix to a string means convert the expression inside the curly brackets {} to their value

    server.sendmail(
        'rishivaya2@gmail.com',
        'rishivaya2@gmail.com',
        msg
    )

    print("Email has benn sent!")

    server.quit()


while (True): # runs the check_price() function at an interval of 1 day
    check_price()
    time.sleep(3600*24)

# check_price()
