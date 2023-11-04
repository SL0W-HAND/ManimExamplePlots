#!/bin/bash

# This script will execute all the python files
for file in *.py; do
    if [ -f "$file" ]; then
        echo "Executing $file..."
        python "$file"
    fi
done
