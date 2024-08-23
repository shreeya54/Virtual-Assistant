import requests
import urllib

def wolf_search(command):
    print('wolf search called')
    pq=urllib.parse.quote_plus(command)
    url=f'http://api.wolframalpha.com/v1/result?appid=6QHAT2-68YWRP2W4R&i={pq}'
    response = requests.get(url)
    print(response.text)
    return response.text