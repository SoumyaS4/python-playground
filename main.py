import datetime
import datetime
import requests
import json
MY_LAT=22.565571
MY_LNG=88.370209
parameters ={
    "lat":MY_LAT ,
    "lng":MY_LNG
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data= response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)

