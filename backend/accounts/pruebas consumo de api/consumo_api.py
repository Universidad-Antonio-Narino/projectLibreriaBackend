import requests

URL = 'http://127.0.0.1:8000/api/login/'

Data= {
    'email': 'eyerforeversam@gmail.com',
    'password': 12345678
}


response = requests.post(URL,Data)
if requests.status_codes == 200:
    print ("Respuesta: ", response.json())
else:
    print("error por: ", response.text)