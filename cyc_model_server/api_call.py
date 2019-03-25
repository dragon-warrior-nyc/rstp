import request

url = 'http://127.0.0.1:5050/api'  # if you are running it locally

payload = {
    "data": {
        "feature_1": [1.0],
        "feature_2": [0.5],
        }
}

r = requests.post(url, json=payload)
r.json()  # it should be the `pred` variable defined in `server.py`
