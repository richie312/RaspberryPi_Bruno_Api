#!/bin/bash

sh /home/pi/Downloads/ngrok.sh

echo "The ngrok session has started. waiting for the public urls to be generated."

echo "The script will be waitin for 30 seconds in order to generate the urls..."

sleep 30

echo "Python script will be executed in order to fetch and get the public urls for video streaming and bruno app."

python ngrok_uri_checker.py

echo "The .env file which contains the url has been sent to the host location."

echo "Giving back the command promt to you..." 