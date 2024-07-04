#!/bin/bash
#Script that takes URL, sends a POST request to passed URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
