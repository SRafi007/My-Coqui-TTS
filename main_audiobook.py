import os
from audiobook.services.tts_service import TTSService

def read_input_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_text(text, chunk_size=500):  # Adjust chunk size as necessary 
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

def main():
    input_file_path = "audiobook/input/input.txt"
    tts_service = TTSService()  # Initialize TTS service
    
    # Read the input text
    text = read_input_file(input_file_path)

    # Get available speakers
    speakers = tts_service.get_speakers()  # Pass the model name to get speakers
    print("Available speakers:", speakers)
    
    filename = "audio.wav"
    tts_service.generate_audio(text, filename, speaker=speakers[0] if speakers else None)

    # Split the text into chunks and generate audio for each chunk (if needed)
    """
    for idx, chunk in enumerate(chunk_text(text)):
        output_filename = f"audiobook_output_chunk_{idx + 1}.wav"  # Just the filename, without the full path
        tts_service.generate_audio(chunk, output_filename, speaker=speakers[0] if speakers else None)
    """

if __name__ == "__main__":
    main()
