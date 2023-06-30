# uvicorn main:app --reload

#Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#Custom Function Imports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check Health
@app.get("/health")
async def check_health():
    return {"message": "healthy"}

# Reset Messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}

# Get audio
@app.get('/post-audio-get/')
async def post_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")

    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)

    # Store messages
    store_messages(message_decoded, chat_response)

    print(chat_response)
    return "Done"

# # Post bot response
# # Note: Not playing in browser when using post request
# @app.post('/post-audio/')
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")
