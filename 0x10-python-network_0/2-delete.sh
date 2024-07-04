#!/bin/bash
#Script to send DELETE request to the URL passed at first argument
curl -s "$1" -X DELETE
