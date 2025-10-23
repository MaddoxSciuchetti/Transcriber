import speech_recognition as sr
from datetime import datetime
import os

# === CONFIG ===
REPORTS_FOLDER = "hvac_reports"  # Folder to store daily logs
LANGUAGE = "de-DE"  # Set "en-US" if you prefer English

# === SETUP ===
os.makedirs(REPORTS_FOLDER, exist_ok=True)
r = sr.Recognizer()

def record_speech():
    """Capture audio input from the microphone."""
    with sr.Microphone() as source:
        print("\n🎙️  Speak your report (press Ctrl+C to stop):")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    return audio

def convert_to_text(audio):
    """Convert recorded speech to text."""
    try:
        text = r.recognize_google(audio, language=LANGUAGE)
        print(f"🗣️  Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("⚠️  Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌  Could not connect to speech recognition service: {e}")
    return None

def save_report(text):
    """Save the recognized text to a timestamped report file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report_{timestamp}.txt"
    filepath = os.path.join(REPORTS_FOLDER, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"HVAC Report – {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        f.write(text + "\n")
    print(f"💾  Report saved: {filepath}")

def main():
    """Run the full voice-to-text process."""
    try:
        audio = record_speech()
        text = convert_to_text(audio)
        if text:
            save_report(text)
    except KeyboardInterrupt:
        print("\n🛑 Recording stopped manually.")

if __name__ == "__main__":
    main()
