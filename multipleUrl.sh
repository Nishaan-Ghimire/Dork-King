#!/bin/bash

# for file with domain collection
if [ $# -eq 0 ]; then
  echo "Please provide a file as an argument."
  exit 1
fi


while IFS= read -r url; do
 
  python3 dorking.py "$url"


  sleep 10

done < "$1"
