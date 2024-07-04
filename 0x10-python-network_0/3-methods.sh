#!/bin/bash
#Script that takes in URL and displays all HTTP methods
curl -s -I -X OPTIONS "$1" | grep "Allows:" | cut -f2- -d" "
