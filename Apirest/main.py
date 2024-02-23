import requests

# aqui me trae estatus 200 quiere decir que esta todo ok 

if __name__ == '__main__':
    url = 'https://www.google.com/?hl=es'
    response = requests.get(url) 
    # print(response)
    
    
    if response.status_code == 200:
        print(response.content)
 
 