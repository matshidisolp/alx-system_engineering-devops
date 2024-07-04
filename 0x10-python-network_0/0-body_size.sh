#!/bin/bash
# send request to given URL
#display the size of the body of the response

curl -s "$1" | wc -c
