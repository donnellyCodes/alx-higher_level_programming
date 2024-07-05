#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -X PUT -d "user_id=98" -H "Origin: You got me!" -L 0.0.0.0:5000/catch_me
