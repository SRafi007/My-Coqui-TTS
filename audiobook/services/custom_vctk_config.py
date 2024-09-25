# custom_vctk_config.py
from dataclasses import dataclass
from TTS.tts.configs.vits_config import VitsConfig, VitsAudioConfig

@dataclass
class CustomVCTKConfig(VitsConfig):
    """Custom VCTK model configuration."""
    
    # You can add custom parameters here if needed
    pass

# Create a custom configuration
custom_config = CustomVCTKConfig(
    model="vctk",
    lr_gen=0.0001,
    lr_disc=0.0001,
    optimizer="Adam",
    num_speakers=10,
    use_speaker_embedding=True,
    
)
