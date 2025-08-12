import os
import time
import re
import google.generativeai as genai

# This assumes the GOOGLE_API_KEY is loaded by main.py
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Error initializing Gemini client: {e}")

def detect_language_gemini(audio_path):
    start = time.time()
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        audio_file = genai.upload_file(path=audio_path)
        
        prompt = """
        Analyze this audio. What is the primary spoken language? 
        Respond with only the IETF language tag (e.g., 'en-US', 'es-ES', 'ta-IN').
        """
        response = model.generate_content([prompt, audio_file])
        
        # We asked for only the language code, so the response should be clean
        language_code = response.text.strip()

        return {
            "provider": "Google Gemini",
            "language": language_code,
            "time_taken": round(time.time() - start, 3),
            "estimated_cost": "$0.001",
            "status": "success",
            "error_message": None,
            "transcript_text": "Transcription not requested" # Updated for clarity
        }
    except Exception as e:
        return {
            "provider": "Google Gemini",
            "language": None,
            "time_taken": round(time.time() - start, 3),
            "estimated_cost": "$0.000",
            "status": "error",
            "error_message": str(e),
            "transcript_text": ""
        }