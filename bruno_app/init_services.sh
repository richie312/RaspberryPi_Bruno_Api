#!/bin/bash

echo "The program is about to start the ngrok session..."

./ngrok start --all

echo "The ngrok session has started. waiting for the public urls to be generated."

echo "Python script will be executed in order to fetch and get the public urls for video streaming and bruno app."

python ngrok_uri_checker.py

echo "The .env file which contains the url has been sent to the host location."

echo "Giving back the command promt to you..." 