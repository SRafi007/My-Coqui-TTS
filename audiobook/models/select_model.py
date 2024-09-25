from TTS.api import TTS

# Define and load all models here
def load_models():
    models = {
        "vctk_vits": {
            "model": TTS(model_name="tts_models/en/vctk/vits"),  # Multi-speaker support
            "speakers": True
        },
        "ljspeech_glow": {
            "model": TTS(model_name="tts_models/en/ljspeech/glow-tts"),  # Single speaker
            "speakers": False
        },
        "ek1_tacotron2_hifigan": {
            "model": TTS(model_name="tts_models/en/ek1/tacotron2"),
            "speakers": False
        },
        "ek1_vits": {
            "model": TTS(model_name="tts_models/en/ek1/vits"),  # Multi-speaker support
            "speakers": True
        },
        "sam_tacotron_ddc": {
            "model": TTS(model_name="tts_models/en/sam/tacotron-DDC"),
            "speakers": False
        },
    }
    return models

def get_model():
    # Load only the desired model; change the model name if necessary
    model_name = "tts_models/en/vctk/vits"  # Change as needed
    try:
        model = TTS(model_name=model_name)
        print(f"Loaded model: {model_name}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def get_speaker_list(model_key):
    model_data = get_model(model_key)
    if model_data and model_data['speakers']:
        return model_data['model'].speakers
    return None
