
#This program converts currency based in the data provided by the API
import json 
import requests
import json
#Put you own API acess key
access_key="f9ed1a120f67cfc66jkj45653d9f100"
base_url=base_url=f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}"

base_currency=input("From currency??")
to_currency=input("To currency??")
quantity=float(input(f"Amount to convert{base_currency}-->{to_currency}??"))

url=base_url+f"&base={base_currency}"+f"&symbol={to_currency}"
response=requests.get(url)
if response.ok is True:
    data=response.json()
    rate=data['rates'][to_currency]
    result=quantity*rate
    print(f"The amount in {to_currency} is ",result)
else:
    print("Could not fetch")

