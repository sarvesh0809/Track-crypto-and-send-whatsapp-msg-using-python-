''' It only scrapes data from coinswitch..,tracks the price and msg if it volatile'''
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client  
account_sid = 'ACf....' #Place your twilio account sid here
auth_token = 'cc6...'    #Place your twilio account token here
client = Client(account_sid, auth_token)           
Doge_coin = requests.get("https://coinswitch.co/coins/dogecoin/dogecoin-to-inr").text #Doge-coin link
btc_link=requests.get("https://coinswitch.co/coins/bitcoin/bitcoin-to-inr").text   #Bit-coin link---->Only need for scraping max and min value.
soup = BeautifulSoup(Doge_coin, 'html.parser')
cryptos = soup.find_all('a', class_="assets__card")
list1 = ['DOGE/INR','BTC/INR']  # You can add multiple crypto's here, i only need 2 so i have added those.
def Doge():    
    high = soup.find_all('h4', class_="content__block__info--data")[1]
    high = float(high.get_text().replace('\t','').replace('INR',''))
    low = soup.find_all('h4', class_="content__block__info--data")[2]
    low = float(low.get_text().replace('\t','').replace('INR',''))
    print(high)     # Max Price in past 24 hrs ... It changes depends of site updates
    print(low)      # Min value in past 24 hrs
    for crypto in cryptos: # for slecting only Doge-coin

        co= crypto.get_text().replace(' ','').split() 
        
        if co[0] in list1[0]:  # list[0]--> Doge-coin
            op1=co[0].replace('/INR','')
            op2=float(co[1].replace('₹',''))
            op3=(f'''Alert!!! {op1} - Price: {op2} ₹''')
            print(op3)   #print current price
    if op2 > (high-0.1) or op2 < (low-0.1) :
        ''' Here it is if loop to compare the current price and send msg    '''
        message = client.messages.create( from_='whatsapp:+1**********',  body=op3, to='whatsapp:+91**********') #Replace * with your twilio no and whatsapp no.
        ''' You can also add multiple whatsapp no here by simply changing variable(message) name and whatsapp no'''        
        print(message.sid)
                
    else:
        print("Everything is fine")     

Doge()
def BTC():
    btc_soup=BeautifulSoup(btc_link,'html.parser') # To find Max and Min values in past 24 hrs.
    high=btc_soup.find_all('h4', class_="content__block__info--data")[1]
    high = float(high.get_text().replace('\t','').replace('INR',''))
    low = btc_soup.find_all('h4', class_="content__block__info--data")[2]
    low = float(low.get_text().replace('\t','').replace('INR',''))
    print(high)
    print(low)
    for crypto in cryptos:
        co= crypto.get_text().replace(' ','').split()
        
        if co[0] in list1[1]:  # list[1]--> Bit-coin
            op1=co[0].replace('/INR','')
            op2=float(co[1].replace('₹',''))
            op3=(f'''Alert!!! {op1} - Price: {op2} ₹''')
            print(op3)
    if op2 > (high-25000) or op2 < (low-50000): #similar as above condition
        message = client.messages.create( from_='whatsapp:+1**********',  body=op3, to='whatsapp:+91**********')        
        print(message.sid)        
    else:
        print("Everything is fine")    
BTC()

'''/// You can add multiple crypto's here by simply changing link and some variable names..///'''
''' That's it'''
