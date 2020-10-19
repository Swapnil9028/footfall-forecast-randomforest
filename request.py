import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Year':2020,'Month':1, 'marketingSpend':20000})

print(r.json())