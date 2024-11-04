#!/bin/bash
DIR=''
files_count=0
while getopts "h?p:" opt; do
case "$opt" in 
	h|\?) 
	echo "Usage: $0 [-p] 'path'"
	exit 0;;
	p) DIR=$OPTARG;;
	esac
done


# Loop through regular files in the directory
for file in $(find "$DIR" -type f -not -type l); do
  # Check if the file has exactly one line
  if [ "$(wc -l < "$file")" > 1 ]; then
    # Increment the counter if it's a one-liner
    ((files_count++))
  fi
done

# Display the result
echo "Number files in $DIR: $files_count"
