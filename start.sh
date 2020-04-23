#!/usr/bin/env bash

# Greetings message
command -v figlet REMOTELY >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
echo Starting Remotely
echo Please, be patient!

# Package checking stage
pip install requirements.txt

# Executing bot
python main.py

