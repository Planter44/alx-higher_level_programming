#!/bin/bash
# Script that shows body size of the response of a curl
curl -so /dev/null -w '%{size_download}\n' "$1"
