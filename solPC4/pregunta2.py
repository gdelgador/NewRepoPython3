from urllib import response
import requests
import json
import sys

URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def get_json(url: str):
    
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException:
        pass

def get_number(msg: str='Ingrese un número decimal: ')->float:
    """Solicita un número decimal"""
    try:
        x = float(input(msg))
        assert x>= 0 # si False, se genera un error y vuelve a solicitar numero 
        
        return x
    except:
        return get_number(msg)

def main():
    
    # cantidad bitcoins >=0
    n = get_number()
    
    # data from url
    data = get_json(URL)
    cost = data['bpi']['USD']['rate_float']
    
    # monto
    amount = cost * n
    print(f"${amount:,.4f}")
    pass


if __name__ == '__main__':
    main()