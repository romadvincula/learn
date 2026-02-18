import os


cert_to_use = os.path.join("home", "arldvincula", "ca-certs", "ca-bundle.pem")
proxies = {
    'http': 'http://webproxy.au.harveynorman.com:8080',
    'https': 'http://webproxy.au.harveynorman.com:8080'
}

