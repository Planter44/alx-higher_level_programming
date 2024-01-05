#!/bin/bash
# Script that takes in a URL and sends a Post to the passed URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
