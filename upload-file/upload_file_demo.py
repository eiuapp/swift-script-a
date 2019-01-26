#!/usr/bin/env python3

import requests
import json
# https://developer.openstack.org/api-ref/identity/v3/index.html?expanded=password-authentication-with-unscoped-authorization-detail#relationships
URL = 'http://192.168.0.50:5000/v3/auth/tokens'
body =  {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": "demo",
                            "domain": {
                                "name": "Default"
                            },
                            "password": "openstack"
                        }
                    }
                }
            }

    
        }
body = {
        "auth": {
                    "identity": {
                                    "methods": [
                                                        "password"
                                                    
                                    ],
                                    "password": {
                                                        "user": {
                                                            "name": "demo",
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
                                                        "name": "demo"
                                                    
                                    }
                                
                    }
                
        }
    
}
body = json.dumps(body)
print(body)
headers = {'Content-Type':'application/json'}
res = requests.post(URL,data=body,headers=headers)
# print(res)
# print(res.headers)
# print(dir(res))
# print(res.text)
# print(res.json())
# print(res.json()["token"])
# print(res.content)
token = res.headers['X-Subject-Token']
# token = res.json()["token"]
# token = res.json()["token"]["audit_ids"][0]
# token = str(token)
print(token)

# https://developer.openstack.org/api-ref/object-store/index.html?expanded=get-object-content-and-metadata-detail,show-account-details-and-list-containers-detail#show-container-details-and-list-objects
# URL = 'http://192.168.0.50:# 8080/v1/'
URL = 'http://192.168.0.50:8080/v1/AUTH_7d6eaa90d74a4f239963933c3a744df3'

headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
res = requests.get(URL,headers=headers)
# #res = requests.put(URL,headers=headers)
print(res.text)


# URL = 'http://192.168.0.50:9292/v2/images'
# headers = {'X-Auth-Token':token,"Content-Type": 'application/json'}
# res = requests.get(URL,headers=headers)
# print(res.text)
# print(res.headers)
print(res.status_code)
