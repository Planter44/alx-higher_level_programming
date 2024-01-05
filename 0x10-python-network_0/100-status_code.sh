#!/bin/bash
# Script that shows size of the URL of the response of a curl request
curl -so /dev/null -w '%{http_code}' "$1"
