# Language Detective Service

A **FastAPI** service that detects the language in an audio file by integrating with multiple AI providers.

## 📦 Setup Instructions

### 1. Install Dependencies

Navigate to the project folder in your terminal and run:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

This project requires API keys to function.
Create a file named `.env` in the root of the project directory and add the following keys, replacing `...` with your actual keys:

```env
OPENAI_API_KEY="..."
GOOGLE_API_KEY="..."
```

---

## 🚀 How to Run the Application

### 1. Start the Server

Once dependencies are installed and `.env` is configured, start the server from the root directory:

```bash
uvicorn main:app --reload
```

### 2. Test the Endpoint

With the server running, send a `POST` request to `/detect/language` using a tool like `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/detect/language" \
-H "Content-Type: application/json" \
-d '{
    "audio_file_path": "path/to/your/audio.mp3",
    "ground_truth_language": "en"
}'
```

---

## 📂 Project Structure (Example)

```
project-root/
│-- main.py
│-- requirements.txt
│-- .env
│-- README.md
└── app/
    ├── routes/
    ├── services/
    └── utils/
```

---

## 🛠 Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* OpenAI API
* Google API

---

## 👤 Author
```
M. Suryakumar
LinkedIn Profile:www.linkedin.com/in/suryakumar-m-aaa891321
```
