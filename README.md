# Voice-to-Text Transcriber (Streamlit App)

A web-based voice transcription tool for creating HVAC reports using speech recognition. Built with Streamlit for an intuitive user interface.

## Features

- 🎙️ **Voice Recording**: Record audio directly through the web interface
- 📝 **Real-time Transcription**: Convert speech to text using Google Speech Recognition
- ✏️ **Edit Transcriptions**: Review and edit transcribed text before saving
- 💾 **Save Reports**: Automatically save reports with timestamps
- 📁 **View History**: Browse and manage recent reports
- 🌍 **Multi-language**: Support for German (de-DE) and English (en-US)

## Setup

1. Install system dependencies (macOS):
   ```bash
   brew install portaudio
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install Python dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Option 1: Using the run script
```bash
./run.sh
```

### Option 2: Direct Streamlit command
```bash
streamlit run transcriber.py
```

The application will open in your default web browser at `http://localhost:8501`

### How to Use:
1. Click the **"🔴 Start Recording"** button
2. Speak your report clearly
3. Wait for the transcription to complete
4. Edit the text if needed
5. Click **"💾 Save Report"** to save
6. View recent reports in the sidebar

## Configuration

You can change settings in the Streamlit UI:
- **Language**: Switch between German (de-DE) and English (en-US)
- Reports are automatically saved in the `hvac_reports/` folder with timestamps

## Requirements

- Python 3.x
- Microphone access
- Internet connection (for Google Speech Recognition API)
- Modern web browser
