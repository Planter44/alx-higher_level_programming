#!/bin/bash
# Script that takes in a URL and shows all HTTP methods the accepted by the server
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
