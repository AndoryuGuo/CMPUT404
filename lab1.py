import requests

#print(requests.__version__)

#  r = requests.get("http://www.google.com")
#  print(r.status_code)
#  print(r.text)

r = requests.get("https://raw.githubusercontent.com/AndoryuGuo/CMPUT404/master/lab1.py")
print(r.text)