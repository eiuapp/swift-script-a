#!/bin/bash

curl -d '{ "auth": { "identity": {"methods": ["password"],"password": {"user": {"name": "admin","domain": {"name": "Default"}, "password": "openstack"}}}}}' -H "Content-type: application/json" http://192.168.0.50:5000/v3/auth/tokens | python -mjson.tool


curl -d '{ "auth": { "identity": {"methods": ["password"],"password": {"user": {"name": "swift","domain": {"name": "default"}, "password": "openstack"}}}}}' -H "Content-type: application/json"  http://192.168.0.50:5000/v3/auth/tokens | python -mjson.tool
