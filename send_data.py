import requests
import time
i = 0

while True:
    response = requests.get(
        "http://localhost:5000/send?idNode=ESP")
    print(i)
    i = i+1
    print(response)
    time.sleep(900)
