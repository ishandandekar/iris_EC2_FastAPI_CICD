import requests

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
}
local_url = "http://0.0.0.0:8000/pred"
remote_url = "https://irispred-cjcntbquza-uc.a.run.app"

resp = requests.get(remote_url, json=data)

print(resp.text)
