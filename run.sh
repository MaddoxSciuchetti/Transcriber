#!/bin/bash
# Activate virtual environment and run Streamlit transcriber

cd "$(dirname "$0")"
source venv/bin/activate
streamlit run transcriber.py
