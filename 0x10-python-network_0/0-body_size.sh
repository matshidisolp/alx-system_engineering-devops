#!/bin/bash
#sends a request to given URL
#displays the size of the body of the response

curl -s "$1" | wc -c
