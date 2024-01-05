#!/bin/bash
# Script that takes in a URL and shows all HTTP methods the accepted by the server
curl -sX GET -H "X-School-User-Id: 98" "$1"
