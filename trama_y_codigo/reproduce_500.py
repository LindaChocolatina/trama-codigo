import requests

url = "http://127.0.0.1:5000/login"
data = {
    "email": "lindasioc@gmail.com",
    "contrasena": "Juanita1509:)",
    "submit": "Ingresar"
}

# Primero obtener el token CSRF
session = requests.Session()
response = session.get(url)
# El token suele estar en un campo oculto 'csrf_token'
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
token = soup.find('input', {'name': 'csrf_token'})['value']
data['csrf_token'] = token

print(f"Sending login request with token {token}...")
response = session.post(url, data=data)

print(f"Status Code: {response.status_code}")
if response.status_code == 500:
    print("REPRODUCED 500 ERROR!")
    print(response.text)
else:
    print("Login attempt finished.")
    print(f"Final URL: {response.url}")
