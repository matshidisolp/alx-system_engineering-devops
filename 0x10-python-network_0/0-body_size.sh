#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign URL from command-line argument
url=$1

# Use curl to fetch the URL and measure the size of the response body
body_size=$(curl -s -o /dev/null -w '%{size_download}' "$url")

# Print the size of the response body
echo "$body_size"
