#!/bin/bash
clear

echo "📦 Installing requirements..."
# Install python if missing
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    pkg install -y python
fi

# Upgrade pip
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# Install all requirements
python3 -m pip install -r requirements.txt --quiet

echo "🚀 Running..."
python3 start.py
