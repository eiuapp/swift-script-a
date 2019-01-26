#!/usr/bin/env python3

import requests
import json
URL = 'http://192.168.0.50:5000/v3/auth/tokens'
body = {
        "auth": {
                    "identity": {
                                    "methods": [
                                                        "password"
                                                    
                                    ],
                                    "password": {
                                                        "user": {
                                                            "name": "admin",
                                            "domain": {
                            "name": "Default"
                                
                                            },
                                            "password": "openstack"
                                                
                                                        }
                                                    
                                    }
                                
                    },
                    "scope": {
                                    "project": {
                                                        "domain": {
                                                                                "name": "Default"
                                                                            
                                                        },
                                                        "name": "admin"
                                                    
                                    }
                                
                    }
                
        }
    
}
body = json.dumps(body)
headers = {'Content-Type':'application/json'}
res = requests.post(URL,data=body,headers=headers)
token =res.headers['X-Subject-Token']
print(token)

URL = 'http://192.168.0.50:8080/v1/AUTH_a640c74e595c44c4902d1c5ebc3afa8a'
URL = 'http://192.168.0.50:8080/v1/AUTH_f04ec0abf3d1460dad82608bb03af589'

headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
res = requests.get(URL,headers=headers)
print(res.text)

# URL = 'http://192.168.0.50:9292/v2/images'
# headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
# res = requests.get(URL,headers=headers)
# print(res.text)
# print(res.headers)
# print(res.status_code)
