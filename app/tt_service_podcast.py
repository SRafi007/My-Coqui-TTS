# /app/tts_service.py
import os
import textwrap
from models.tts_model_selector import load_tts_model
from TTS.api import TTS


def generate_tts(text, output_path, purpose, gender):
    speaker = 'speaker_name_for_female' if gender == 'female' else 'speaker_name_for_male'
    available_speakers = tts.synthesizer.speaker_manager.speakers
    
    if speaker not in available_speakers:
        print(f"Speaker '{speaker}' not found. Using default speaker.")
        speaker = available_speakers[0]  # fallback to the first available speaker
    
    tts.tts_to_file(text=text, file_path=output_path, speaker=speaker)



# Helper function to chunk text into smaller parts
def chunk_text(text, max_chars=200):
    """Break text into smaller chunks."""
    return textwrap.wrap(text, width=max_chars)
