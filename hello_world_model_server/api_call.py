import requests

url = 'http://127.0.0.1:5050/api'  # if you are running it locally

payload = {
    "message": "this is the first rest api"
}

r = requests.post(url, json=payload)
r.json()  # it should be the `pred` variable defined in `server.py`

r = requests.get(url)
r.json()
