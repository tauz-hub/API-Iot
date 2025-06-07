import requests

public_url = "https://84e4-34-139-246-233.ngrok-free.app"

dado1 = {"temperatura": 25, "umidade": 60}
dado2 = {"temperatura": 27, "umidade": 58}
dado3 = {"temperatura": 29, "umidade": 55}

requests.post(f"{public_url}/visualize", json=dado1)
requests.post(f"{public_url}/visualize", json=dado2)
requests.post(f"{public_url}/visualize", json=dado3)

res = requests.get(f"{public_url}/data")
print(res.json())