#!/bin/bash
set -e  # Stop script on error

echo "Restarting React Frontend..."

# install dependencies
npm install

# Start React frontend in development mode
npm start

echo "React frontend is running!"