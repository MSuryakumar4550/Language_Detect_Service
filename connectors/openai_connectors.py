import os
import time
from openai import OpenAI

# Initialize the OpenAI client.
# This assumes the OPENAI_API_KEY is already loaded into the environment.
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    # This will print an error if the key is missing when the app starts.
    print(f"Error initializing OpenAI client: {e}")
    client = None


def detect_language_openai(audio_path):
    """
    Transcribes an audio file using OpenAI's Whisper model and identifies the language.
    """
    start = time.time()
    if not client:
        return {
            "provider": "OpenAI",
            "language": None,
            "time_taken": 0,
            "estimated_cost": "$0.000",
            "status": "error",
            "error_message": "OpenAI client not initialized. Check API key.",
            "transcript_text": "",
        }

    try:
        with open(audio_path, "rb") as audio_file:
            # Call the Whisper API for transcription
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",  # Ensures the language field is always returned
            )

        return {
            "provider": "OpenAI",
            "language": transcript.language,
            "time_taken": round(time.time() - start, 3),
            "estimated_cost": "$0.002",  # Placeholder cost
            "status": "success",
            "error_message": None,
            "transcript_text": transcript.text,
        }
    except Exception as e:
        return {
            "provider": "OpenAI",
            "language": None,
            "time_taken": round(time.time() - start, 3),
            "estimated_cost": "$0.000",
            "status": "error",
            "error_message": str(e),
            "transcript_text": "",
        }