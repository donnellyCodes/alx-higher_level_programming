#!/bin/bash
#Script that takes in URL as an argument, send GET request to the URL
curl -sH "X-School-User-Id: 98" "$1"
