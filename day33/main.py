#100 - wait
#200 - confirm
#300 - u dont have acess
#400 - the req doesnt exist (user fault)
#500 - the server is down


import requests

response =requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data =response.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss=(latitude,longitude)
print(iss)
