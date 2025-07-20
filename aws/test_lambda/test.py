# test calling the lambda function locally

import requests


# # url for the local lambda function
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# url for api gateway
url = 'https://5ububpyv3g.execute-api.ap-southeast-2.amazonaws.com/test/predict'

proxies = {
    'http': 'http://webproxy.au.harveynorman.com:8080',
    'https': 'http://webproxy.au.harveynorman.com:8080', # Use http for https proxies if it's a standard HTTP proxy
}
use_proxy = True

# payload to send to the lambda function
data = {"url": "dummy_predictor_url"}

if use_proxy:
    result = requests.post(url, json=data, proxies=proxies, verify=False).json()
else:
    result = requests.post(url, json=data).json()

print(result)