import requests

url = "http://127.0.0.1:5000"

sum = {"num": 2, "num2": 3}

response = requests.post(f"{url}/somar", json=sum)

if response.status_code == 200:
    result = response.json()["resultado"]
    print(f"{result}")

else:
    print("Erro", response.text)
