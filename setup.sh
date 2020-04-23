#!/usr/bin/env bash

# Greetings message
command -v figlet REMOTELY >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
echo Please wait a minute

# Renaming example configuration to configuration
mv example.config.py config.py

# Announcing that task is completed
echo "Done, now insert your own credentials to conf file!"
