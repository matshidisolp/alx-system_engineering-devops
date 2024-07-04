#!/bin/bash
# send request to given URL
#displa the size of the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s "$1" | wc -c
