import requests
from bs4 import BeautifulSoup

payload={}
headers={
    "apikey": "Lx6GP1NytbeGoEIGdFhCCuPseF3RcWKV"
}
def getData(url):
    r = requests.request('GET',url,headers=headers,data=payload)
    return r.text

number = int(input("Enter The NUmber : "))

htmldata = getData('https://api.apilayer.com/number_verification/validate?number=+91'+str(number))
soup = BeautifulSoup(htmldata,'html.parser')
print(soup)