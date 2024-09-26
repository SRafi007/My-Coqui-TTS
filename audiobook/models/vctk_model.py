# models/vctk_model.py
from TTS.api import TTS

class VCTKModel:
    def __init__(self):
        self.model_name = "tts_models/en/vctk/vits"
        self.model = TTS(model_name=self.model_name)
        print(f"Loaded model: {self.model_name}")

    def get_speakers(self):
        return self.model.speakers
    
    def text_to_speech(self, text, output_path, speaker):
        self.model.tts_to_file(text=text, speed=0.8, file_path=output_path, speaker=speaker,emotion='happy')
