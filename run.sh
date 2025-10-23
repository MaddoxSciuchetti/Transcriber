#!/bin/bash
# Activate virtual environment and run transcriber

cd "$(dirname "$0")"
source venv/bin/activate
python transcriber.py
