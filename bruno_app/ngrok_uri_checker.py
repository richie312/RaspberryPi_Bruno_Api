import requests
ngrok_base_url = "http://127.0.0.1:4040/api"

response = request.get(ngrok_base_url + '/tunnels')

result = response.json()
print(result)
