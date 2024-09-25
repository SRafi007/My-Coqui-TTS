# models/ek1_model.py
from TTS.api import TTS

class EK1Model:
    def __init__(self):
        self.model_name = "tts_models/en/ek1/tacotron2"  # Updated model name
        self.model = TTS(model_name=self.model_name)
        print(f"Loaded model: {self.model_name}")

    def get_speakers(self):
        return self.model.speakers

    def tts_to_file(self, text, output_path, speaker=None):
        self.model.tts_to_file(text=text, file_path=output_path, speaker=speaker)
