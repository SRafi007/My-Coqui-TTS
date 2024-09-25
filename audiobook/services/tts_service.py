# services/tts_service.py
import os
from audiobook.models.vctk_model import VCTKModel  # Import the specific model
from audiobook.models.ek1_model import EK1Model
from audiobook.models.fastspeech2_model import FastSpeech2Model
from audiobook.models.ljspeech_model_neural_hmm import LJSpeechModel

class TTSService:
    def __init__(self, model_class=VCTKModel):
        """Initialize the TTS service with a specified model class."""
        self.model_instance = model_class()  # Create an instance of the model
        self.output_dir = "audiobook/output"
        os.makedirs(self.output_dir, exist_ok=True)  # Ensure output directory exists

    def get_speakers(self):
        """Get the list of speakers for the loaded model."""
        return self.model_instance.get_speakers()

    def generate_audio(self, text, filename, speaker=None):
        """Generate audio from text and save it to a file."""
        output_path = os.path.join(self.output_dir, filename)
        speakers=self.model_instance.get_speakers()
        print(type(speakers))
        # Check if the model is multi-speaker and a speaker is provided
        if self.model_instance.get_speakers() and not speaker:
            raise ValueError("Model is multi-speaker but no `speaker` is provided.")
        
        # Generate audio file
        self.model_instance.tts_to_file(text=text, output_path=output_path, speaker=speakers[5])
        print(f"Generated audio saved to {output_path}.")
