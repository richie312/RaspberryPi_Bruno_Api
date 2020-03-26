#!/bin/bash

echo "changing directory to instantiate the ngrok service."

cd ..

lxterminal -e sh /home/pi/Downloads/ngrok.sh & ...

echo "The ngrok session has started. waiting for the public urls to be generated."

echo "The script will be waitin for 10 seconds in order to generate the urls..."

sleep 10

echo "Moving back to app folder."

cd bruno_app

echo "Python script will be executed in order to fetch and get the public urls for video streaming and bruno app."

python3 ngrok_uri_checker.py

echo "The .env file which contains the url has been sent to the host location."

echo "Changing Directory to run the bruno application"

cd ..
cd raspberry_files

echo "Changing Directory to run the bruno application"
echo "executing the python application..."

lxterminal -e python main.py & ...

echo "Changing Directory to stream the video"

cd .. && cd mjpg-streamer/mjpg-streamer-experimental/

lxterminal -e ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"

echo "changing directory to root folder"

cd ../.. && cd bruno_app

echo "Giving back the command promt to you..." 