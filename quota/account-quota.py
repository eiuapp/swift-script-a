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

# admin publicURL
# URL = 'http://192.168.0.50:8080/v1/AUTH_f04ec0abf3d1460dad82608bb03af589'

# utest1 publicURL
controller="192.168.0.50"
URL = "http://" + controller + ":8080/v1/AUTH_e8ed1722599643b5802a322341b4e02c"
# print(URL)

# set quota
headers = {'X-Auth-Token':token,"Content-Type": 'application/json', "X-Account-Meta-Quota-Bytes": "1234567"}
res = requests.post(URL,headers=headers)
print(res.status_code)
# get quota
headers = {'X-Auth-Token':token}
res_head = requests.head(URL,headers=headers)
print(res_head.status_code)
print(res_head.headers)
# get quota and container list
headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
res_get = requests.get(URL,headers=headers)
print(res_get.status_code)
print(res_get.headers)
print(res_get.text)

# URL = 'http://192.168.0.50:9292/v2/images'
# headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
# res = requests.get(URL,headers=headers)
# print(res.text)
# print(res.headers)
# print(res.status_code)
