__author__ = 'andreas'
#imports the function to load websites
import urllib.request
#imports the time library
import time

#define the get_price function
def get_price():
    #loads the website and decodes it with UTF8 to make it readable
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    #looks for the beginning of the price
    price_position = text.find(">$")
    #calculates the position of the price
    price_beginning = price_position + 2
    price_end = price_beginning + 4
    #gives the current price as output
    return float(text[price_beginning:price_end])

price_now = input("Do you need the price immediately? (Y/n)")
if price_now in ("Y","y"):
    print(get_price())
else:
    #the variable price needs a start value otherwise the loop won't work.
    price = 99.99
    #A loop to the check the coffee2 prices
    while price > 4.74:
        #wait for 15 minutes
        time.sleep(900)
        #call the get_price function and assign it's output to the variable prcice
        price = get_price()
    print("Buy!")
