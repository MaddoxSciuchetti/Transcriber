import streamlit as st
import speech_recognition as sr
from datetime import datetime
import os
import glob

# === CONFIG ===
REPORTS_FOLDER = "hvac_reports"
LANGUAGE = "de-DE"

# === SETUP ===
os.makedirs(REPORTS_FOLDER, exist_ok=True)

# Initialize session state
if 'transcribed_text' not in st.session_state:
    st.session_state.transcribed_text = ""
if 'recording_status' not in st.session_state:
    st.session_state.recording_status = ""

def record_speech():
    """Capture audio input from the microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.session_state.recording_status = "🎙️ Adjusting for ambient noise..."
        r.adjust_for_ambient_noise(source, duration=1)
        st.session_state.recording_status = "🎙️ Listening... Speak now!"
        audio = r.listen(source)
        st.session_state.recording_status = "✅ Recording complete!"
    return audio, r

def convert_to_text(audio, recognizer):
    """Convert recorded speech to text."""
    try:
        text = recognizer.recognize_google(audio, language=LANGUAGE)
        return text, None
    except sr.UnknownValueError:
        return None, "⚠️ Could not understand audio. Please try again."
    except sr.RequestError as e:
        return None, f"❌ Could not connect to speech recognition service: {e}"

def save_report(text):
    """Save the recognized text to a timestamped report file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report_{timestamp}.txt"
    filepath = os.path.join(REPORTS_FOLDER, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"HVAC Report – {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        f.write(text + "\n")
    return filepath

def get_saved_reports():
    """Get list of all saved reports."""
    reports = glob.glob(os.path.join(REPORTS_FOLDER, "report_*.txt"))
    return sorted(reports, reverse=True)

def main():
    """Main Streamlit application."""
    st.set_page_config(
        page_title="HVAC Voice Transcriber",
        page_icon="🎙️",
        layout="wide"
    )
    
    st.title("🎙️ HVAC Voice Transcriber")
    st.markdown("Record your HVAC reports using voice and save them automatically.")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        language = st.selectbox(
            "Language",
            ["de-DE", "en-US"],
            index=0 if LANGUAGE == "de-DE" else 1
        )
        st.divider()
        st.header("📊 Statistics")
        reports = get_saved_reports()
        st.metric("Total Reports", len(reports))
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎤 Record New Report")
        
        if st.button("🔴 Start Recording", type="primary", use_container_width=True):
            with st.spinner("Recording in progress..."):
                try:
                    audio, recognizer = record_speech()
                    st.success(st.session_state.recording_status)
                    
                    with st.spinner("Converting speech to text..."):
                        text, error = convert_to_text(audio, recognizer)
                        
                        if text:
                            st.session_state.transcribed_text = text
                            st.success("✅ Transcription complete!")
                        else:
                            st.error(error)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        # Display transcribed text
        if st.session_state.transcribed_text:
            st.subheader("📝 Transcribed Text")
            edited_text = st.text_area(
                "Edit if needed:",
                value=st.session_state.transcribed_text,
                height=200,
                key="text_editor"
            )
            
            col_save, col_clear = st.columns(2)
            with col_save:
                if st.button("💾 Save Report", type="primary", use_container_width=True):
                    filepath = save_report(edited_text)
                    st.success(f"✅ Report saved: {os.path.basename(filepath)}")
                    st.session_state.transcribed_text = ""
                    st.rerun()
            
            with col_clear:
                if st.button("🗑️ Clear", use_container_width=True):
                    st.session_state.transcribed_text = ""
                    st.rerun()
    
    with col2:
        st.header("📁 Recent Reports")
        
        if reports:
            for report_path in reports[:5]:  # Show last 5 reports
                report_name = os.path.basename(report_path)
                with st.expander(report_name):
                    with open(report_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    st.text(content)
                    
                    if st.button(f"🗑️ Delete", key=f"delete_{report_name}"):
                        os.remove(report_path)
                        st.success(f"Deleted {report_name}")
                        st.rerun()
        else:
            st.info("No reports yet. Start recording to create your first report!")

if __name__ == "__main__":
    main()
