import requests
import os


def download_file(file):
    environ = os.environ.get('ENVIRON')
    res = requests.get(f"https://data.gharchive.org/{file}", verify=False) if environ == 'DEV' else requests.get(f"https://data.gharchive.org/{file}")
    return res

if __name__ == "__main__":
    res = download_file('2021-01-29-0.json.gz')
    print(res.status_code)

