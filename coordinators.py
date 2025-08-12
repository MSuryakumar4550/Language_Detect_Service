from connectors.openai_connectors import detect_language_openai
from connectors.elevenLabs_connectors import detect_language_elevenlabs 
from connectors.sarvam_connectors import detect_language_sarvam 
from connectors.gemini_connectors import detect_language_gemini

def run_all(audio_path):
    results = {
        "openai": detect_language_openai(audio_path),
        "elevenlabs": detect_language_elevenlabs(audio_path),
        "sarvam": detect_language_sarvam(audio_path),
        "gemini": detect_language_gemini(audio_path)
    }
    return results