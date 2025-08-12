from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load all environment variables from .env before doing anything else
load_dotenv()

# Now import your other modules
from coordinators import run_all


app = FastAPI()

class DetectRequest(BaseModel):
    audio_file_path: str
    ground_truth_language: str

@app.post("/detect/language")
def detect_language(req: DetectRequest):
    # Check if the audio file exists before processing
    if not os.path.exists(req.audio_file_path):
        raise HTTPException(status_code=404, detail="Audio file not found at the specified path.")

    # Call the coordinator function with the audio path from the request
    results_dict = run_all(req.audio_file_path)
    
    # Format the dictionary from run_all into a list for the JSON response
    results_list = []
    for provider_name, data in results_dict.items():
        results_list.append(data)
        
    return results_list

@app.get("/")
def home():
    return {"message": "Language Detective Service is running."}