# Voice-to-Text Transcriber

A standalone voice transcription tool for creating HVAC reports using speech recognition.

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

Run the transcriber:
```bash
python transcriber.py
```

- Speak your report when prompted
- Press `Ctrl+C` to stop recording
- Reports are saved in the `hvac_reports/` folder with timestamps

## Configuration

Edit `transcriber.py` to change:
- `LANGUAGE`: Default is "de-DE" (German), change to "en-US" for English
- `REPORTS_FOLDER`: Where reports are saved

## Requirements

- Python 3.x
- Microphone access
- Internet connection (for Google Speech Recognition API)
