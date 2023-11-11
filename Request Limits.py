import requests
import json
import sys
from urllib.parse import urljoin

API_BASE = "https://api.waas.barracudanetworks.com/v4/waasapi/"

def waas_api_get(token, path):
    res = requests.get(urljoin(API_BASE, path), headers={"Content-Type": "application/json", "auth-api": token})
    res.raise_for_status()
    return res.json()


def waas_api_patch(token, path, data):
    res = requests.patch(urljoin(API_BASE, path), data, headers={"Content-Type": "application/json", "auth-api": token})
    res.raise_for_status()
    return res.json()


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        token = sys.argv[1]
    else:
        token = input("Enter API Token:")


# Testing - Request Limits 

#patch request limits - max number of headers
data = json.dumps({"max_number_of_headers": 40})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/request_limits/', data)
print('updated config:', json.dumps(updated, indent=4))

#get request limits - max number of headers
get = waas_api_get(token, urljoin(API_BASE, 'applications/dvwa.darklab.co/request_limits/'))
print('get result:', json.dumps(get, indent=4))
