import requests
import json
import os
import dotenv
main_dir = os.getcwd()
ngrok_base_url = "http://127.0.0.1:4040/api"

response = requests.get(ngrok_base_url + '/tunnels')
response_obj = response.json()

# get the uri for videostream and bruno_app

# collect the index number for bruno app url (any one url)
for i in range(len(response_obj['tunnels'])):
    if response_obj['tunnels'][i]['name'] == 'bruno-app':
        bruno_app_url_index = i

bruno_app_url = response_obj['tunnels'][bruno_app_url_index]['public_url']

# collect the index for the video stream_url

for j in range(len(response_obj['tunnels'])):
    if response_obj['tunnels'][j]['name'] == 'video-stream':
        video_stream_url_index = j
        
video_stream_url = response_obj['tunnels'][video_stream_url_index]['public_url']

# dump the urls in the .env files

# set the parent path for the dot_env
dot_env_path = main_dir
url_dict  = {'bruno_app_url' : bruno_app_url, 
            'video_stream_url': video_stream_url}
key_list = list(url_dict.keys())
# generate the keys and save it in .env file
[dotenv.set_key(os.path.join(dot_env_path,'.env'),key_list[i],url_dict[key_list[i]]) for i in range(len(key_list))]
