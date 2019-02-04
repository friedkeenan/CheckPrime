#!/usr/bin/env python3

import requests

num=int(input("Number to check: "))
r=requests.get("https://numberempire.com/"+str(num))
r=r.text
r=r.split("Is prime?",1)[1]
r=r.split("</span>",1)[0]
r=(r[-1]=="S")
if r:
    print(str(num)+" is prime!")
else:
    print(str(num)+" is not prime, you idiot")
