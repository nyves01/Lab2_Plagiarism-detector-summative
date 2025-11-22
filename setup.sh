#!/bin/bash

if [ ! -d "essays" ]; then
    mkdir essays
    echo "$(date): Created essays directory" >> setup.log
else
    echo "$(date): essays directory already exists" >> setup.log
fi

if [ ! -d "reports" ]; then
    mkdir reports
else
    echo "$(date): reports directory already exists" >> setup.log
fi

echo "$(date): Setup completed successfully" >> setup.log
