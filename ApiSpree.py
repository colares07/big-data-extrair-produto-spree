import json, requests, time

class ApiSpree:
    _END_POINT = '/api/v1/products'

    def __init__(self, token, url='http://localhost:5000'):
        self._token = token
        self._url = url
        self.custom_header = {'X-Spree-Token': self._token, 'content-type': 'application/json'}

    def getListaProduto(self, loop=1):
        print('loop '+ str(loop))
        print(self._url+self._END_POINT)
        
        try: 
           opt = requests.options(self._url+self._END_POINT, headers=self.custom_header)
        except:
           time.sleep(loop)
           self.getListaProduto(loop=(loop+1)) 

        req = requests.get(self._url+self._END_POINT, headers=self.custom_header)
        return req.json()['products']

