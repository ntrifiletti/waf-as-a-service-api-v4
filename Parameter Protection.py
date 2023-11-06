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


# Testing - Enable/Disable Parameter Protection Attack Libraries

#patch sql injection
data = json.dumps({"sql_injection": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch os command injection
data = json.dumps({"os_command_injection": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch XSS
data = json.dumps({"cross_site_scripting": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch RFI 
data = json.dumps({"remote_file_inclusion": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch ldap injection
data = json.dumps({"ldap_injection": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch php attacks
data = json.dumps({"python_php_attacks": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch http specific
data = json.dumps({"http_specific_injection": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#patch apache struts
data = json.dumps({"apache_struts_attacks": "normal"})
updated = waas_api_patch(token, 'applications/dvwa.darklab.co/parameter_protection/', data)


#get summary of Parameter protection
get = waas_api_get(token, urljoin(API_BASE, 'applications/dvwa.darklab.co/parameter_protection/'))
print('get result:', json.dumps(get, indent=4))