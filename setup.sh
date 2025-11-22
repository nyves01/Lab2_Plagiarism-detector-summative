#!/bin/bash

# Create essays directory if it doesn't exist
if [ ! -d "essays" ]; then
    mkdir essays
    echo "$(date): Created essays directory" >> setup.log
else
    echo "$(date): essays directory already exists" >> setup.log
fi

# Create reports directory if it doesn't exist
if [ ! -d "reports" ]; then
    mkdir reports
else
    echo "$(date): reports directory already exists" >> setup.log
fi

# Indicate completion of setup
echo "$(date): Setup completed successfully" >> setup.log