import requests

parms = {'username':'Ryan',
         'password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",parms)
print("cookie is set to:")
print(r.cookies.get_dict())
print("-----------------")
print("Going to profile page..")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies = r.cookies)
print(r.text())