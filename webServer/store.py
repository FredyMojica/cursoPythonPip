import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # estado
    print(r.text) # saber la respuesta, el retorno
    print(type(r.text)) # Que tipo de datos tenemos
    categories = r.json() # Convertirlo a un formato python json
    for category in categories:
        print(category['name'])