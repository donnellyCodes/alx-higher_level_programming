#!/bin/bash
#Script that takes in URL, send request to the URL, displays size of the body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
