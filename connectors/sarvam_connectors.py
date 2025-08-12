import time

def detect_language_sarvam(audio_path):
    start = time.time()
    return {
        "provider": "Sarvam AI",
        "language": "ta",
        "time_taken": round(time.time() - start, 2),
        "estimated_cost": "$0",
        "status": "success",
        "error_message": None
    }
